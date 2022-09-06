namespace KidneyCarcinomaRestApi.Models.Errors
{
    using Newtonsoft.Json;

    public class JsonErrorResponseData
    {
        [JsonProperty("message")]
        public string Message { get; set; }
        
        [JsonProperty("parameter")]
        public string Parameter { get; set; }
        
        [JsonProperty("value")]
        public string Value { get; set; }
        
        [JsonProperty("queryString")]
        public string Query { get; set; }
        
        [JsonProperty("code")]
        public int StatusCode { get; set; }
    }
}