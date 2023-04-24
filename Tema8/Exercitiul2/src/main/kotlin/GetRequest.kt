import khttp.get
import khttp.responses.Response

class GetRequest(url: String, params: Map<String, String>?, private val timeout: Int): HTTPGet {
    private val genericReq: GenericRequest = GenericRequest(url, params)

    override fun getResponse(): Response {
        return if (genericReq.params == null) {
            get(genericReq.url, timeout=timeout.toDouble())
        } else {
            get(genericReq.url, params=genericReq.params, timeout=timeout.toDouble())
        }
    }
}