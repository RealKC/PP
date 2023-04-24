import khttp.responses.Response

class CleanGetRequest(private val getRequest: GetRequest): HTTPGet {
    private val parentalControlDisallow: List<String> = listOf()
    private var cachedResponse: Response? = null

    override fun getResponse(): Response {
        if (cachedResponse == null) {
            cachedResponse = getRequest.getResponse()
        }

        if (parentalControlDisallow.contains(cachedResponse!!.url)) {
            throw RuntimeException("Disallowed url!!")
        }

        return cachedResponse!!
    }
}