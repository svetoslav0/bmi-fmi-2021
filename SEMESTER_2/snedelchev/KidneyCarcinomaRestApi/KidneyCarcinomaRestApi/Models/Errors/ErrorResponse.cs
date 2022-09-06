namespace KidneyCarcinomaRestApi.Models.Errors
{
    using System.Collections.Generic;

    using Newtonsoft.Json;

    public class ErrorResponse
    {
        [JsonProperty("errors")]
        public List<JsonErrorResponseData> ErrorData { get; set; }
    }
}