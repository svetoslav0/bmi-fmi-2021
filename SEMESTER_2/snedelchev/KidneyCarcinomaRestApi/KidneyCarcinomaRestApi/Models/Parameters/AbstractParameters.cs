namespace KidneyCarcinomaRestApi.Models.Parameters
{
    using Microsoft.AspNetCore.Mvc;

    public class AbstractParameters
    {
        [FromQuery(Name = "limit")]
        public int Limit { get; set; }
        
        [FromQuery(Name = "offset")]
        public int? Offset { get; set; }
    }
}