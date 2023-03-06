import polyglot
import subprocess


def r_main(output, colour):
    lin_reg = polyglot.eval(language="R", string="""
main <- function(output, colour) {
    library("lattice")

    data <- read.csv('dataset.txt')

    svg(output)
    print(xyplot(x ~ y, data, type = c("p", "r"), col = colour))
    dev.off()
}
""")
    lin_reg(output, colour)


def main():
    output_name = input('Name of file to output to: ')
    output_path = input('Path to output to: ')
    colour = input('Input the colour for the points: ')

    output = output_path + '/' + output_name
    if not output.endswith('.svg'):
        output = output + '.svg'
    r_main(output, colour)

    subprocess.run(['xdg-open', output])


if __name__ == '__main__':
    main()
