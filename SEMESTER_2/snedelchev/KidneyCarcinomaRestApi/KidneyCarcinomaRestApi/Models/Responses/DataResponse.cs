namespace KidneyCarcinomaRestApi.Models.Responses
{
    using Newtonsoft.Json;

    public class DataResponse
    {
        [JsonProperty("data")]
        public object Data { get; set; }
    }
}