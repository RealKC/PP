class GenericRequest(val url: String, val params: Map<String, String>?): Cloneable {
    public override fun clone(): Any {
        return super.clone()
    }
}