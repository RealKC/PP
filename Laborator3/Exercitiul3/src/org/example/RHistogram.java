package org.example;

import static java.awt.image.BufferedImage.TYPE_INT_RGB;
import java.awt.Color;
import java.awt.Graphics2D;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;
import org.graalvm.polyglot.Context;
import org.graalvm.polyglot.Value;

public class RHistogram {
    private static final int WIDTH = 1000;
    private static final int HEIGHT = 500;

    public static <E> void writeImage(Value showPlot, String fname, E[] values) {
        BufferedImage image = new BufferedImage(WIDTH, HEIGHT, TYPE_INT_RGB);
        Graphics2D graphics = (Graphics2D) image.getGraphics();
        graphics.setBackground(new Color(255, 255, 255));
        graphics.clearRect(0, 0, WIDTH, HEIGHT);
        showPlot.execute(graphics, WIDTH, HEIGHT, values);

        try {
            ImageIO.write(image, "png", new File(fname + ".png"));
        } catch (IOException e) {
            e.printStackTrace();
        }
        System.out.println("SUCCESS : [" + fname + "]");
    }

    public static <E> void buildHistogram(E[] values, String fname, boolean how) {
        Context context = Context.newBuilder("R").allowAllAccess(true).build();
        String src;

        if (how) {
            src = """
                library(lattice)
                function(g, w, h, data) {
                    grDevices::awt(w, h, g)
                    B <- c(data)
                    tab <- table(B)
                    print(barchart(tab))
                    dev.off()
                }
        """;
        } else {
            src = """
                library(lattice)
                function(g, w, h, data) {
                    grDevices::awt(w, h, g)
                    B <- c(data)
                    x <- 0:(length(B) - 1)
                    print(xyplot(B ~ x))
                    dev.off()
                }
        """;
        }

        Value showPlot = context.eval("R", src);

        writeImage(showPlot, fname, values);

        context.close();
    }
}