fun main(args: Array<String>) {
    val browser = KidsBrowser(
        CleanGetRequest(
            GetRequest("https://google.com/search", mapOf("q" to "wikipedia"), 5)),
        PostRequest("https://en.wikipedia.org", null))

    browser.start()
}