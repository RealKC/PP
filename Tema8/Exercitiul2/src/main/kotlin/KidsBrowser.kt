class KidsBrowser(private val clearReq: CleanGetRequest, private val postReq: PostRequest?) {
    fun start() {
        if (postReq != null) {
            println("Posted: '${postReq.postData().text}'")
        }

        println("Got: '${clearReq.getResponse().text}'")
    }
}