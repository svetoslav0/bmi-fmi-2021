#nullable enable
namespace KidneyCarcinomaRestApi.Models
{
    using MongoDB.Bson;
    using MongoDB.Bson.Serialization.Attributes;
    using Newtonsoft.Json;

    [BsonIgnoreExtraElements]
    public class Case
    {
        [BsonId]
        [BsonRepresentation(BsonType.ObjectId)]
        [Newtonsoft.Json.JsonIgnore]
        public string? Id { get; set; }
        
        [BsonElement("case_id")]
        [JsonProperty("case_id")]
        public string CaseId { get; set; }

        [BsonElement("demographic")]
        [JsonProperty("demographic")]
        public Demographic? Demographic { get; set; }

        [BsonElement("exposure_ids")]
        [JsonProperty("exposure_ids")]
        public string[]? ExposureIds { get; set; }

        [BsonElement("diagnosis_ids")]
        [JsonProperty("diagnosis_ids")]
        public string[]? DiagnosesIds { get; set; }
    }
}
