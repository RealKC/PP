import org.jsoup.Jsoup

data class RssFeed(
    val title: String,
    val link: String,
    val description: String,
    val items: List<RssFeedItem>
) {
    override fun toString(): String {
        var builder = StringBuilder()

        builder.append("$title (@ $link)\n$description\n")

        for (item in items.withIndex()) {
            builder.append("#${item.index}. ${item.value}\n")
        }

        return builder.toString()
    }
}

data class RssFeedItem(
    val title: String,
    val link: String,
    val description: String,
    val pubDate: String,
) {
    override fun toString(): String {
        return "$title on $pubDate (@ $link):\n\t$description"
    }
}

fun main(args: Array<String>) {
    val document = Jsoup.connect("https://this-week-in-rust.org/rss.xml").get()

    val rssItems = document.select("item").map {
        val title = it.select("title").text()
        val link = it.select("link").text()
        val description = it.select("description").text()
        val pubDate = it.select("pubDate").text()

        RssFeedItem(title, link, description, pubDate)
    }
    val title = document.select("title")[0]!!.text()
    val link = document.select("link")[0]!!.text()
    val description = document.select("description")[0]!!.text()

    val rssFeed = RssFeed(title, link, description, rssItems)

    println(rssFeed)
}