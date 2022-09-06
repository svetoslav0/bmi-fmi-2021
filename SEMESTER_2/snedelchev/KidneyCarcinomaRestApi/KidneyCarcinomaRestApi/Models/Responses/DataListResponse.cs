namespace KidneyCarcinomaRestApi.Models.Responses
{
    using Newtonsoft.Json;

    public class DataListResponse : DataResponse
    {
        [JsonProperty("total")]
        public long Total { get; set; }
    }
}