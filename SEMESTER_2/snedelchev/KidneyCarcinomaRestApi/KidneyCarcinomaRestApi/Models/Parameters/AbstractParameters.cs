namespace KidneyCarcinomaRestApi.Models.Parameters
{
    using Microsoft.AspNetCore.Mvc;

    public class AbstractParameters
    {
        [FromQuery(Name = "limit")]
        public int Limit { get; set; }
        
        [FromQuery(Name = "offset")]
        public int? Offset { get; set; }
        
        public void Deconstruct(
            out int limit,
            out int offset)
        {
            limit = this.Limit;
            offset = this.Offset.HasValue ? this.Offset.Value : 0;
        }
    }
}