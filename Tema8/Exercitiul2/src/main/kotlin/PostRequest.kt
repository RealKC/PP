import khttp.post
import khttp.responses.Response

class PostRequest(url: String, params: Map<String, String>?) {
    private val genericReq = GenericRequest(url, params)

    fun postData(): Response {
        return if (genericReq.params != null) {
            post(genericReq.url, params=genericReq.params)
        } else {
            post(genericReq.url)
        }
    }
}