#nullable enable
namespace KidneyCarcinomaRestApi.Models
{
    using System;

    using MongoDB.Bson.Serialization.Attributes;
    using Newtonsoft.Json;

    [BsonIgnoreExtraElements]
    public class Demographic
    {
        [BsonElement("demographic_id")]
        [JsonProperty("demographic_id")]
        public string? DemographicId { get; set; }

        [BsonElement("race")]
        [JsonProperty("race")]
        public string? Race { get; set; }

        [BsonElement("gender")]
        [JsonProperty("gender")]
        public string? Gender { get; set; }

        [BsonElement("ethnicity")]
        [JsonProperty("ethnicity")]
        public string? Ethnicity { get; set; }

        [BsonElement("vital_status")]
        [JsonProperty("vital_status")]
        public string? VitalStatus { get; set; }

        [BsonElement("age_at_index")]
        [JsonProperty("age_at_index")]
        public int? AgeAtIndex { get; set; }

        [BsonElement("submitter_id")]
        [JsonProperty("submitter_id")]
        public string? SubmitterId { get; set; }

        [BsonElement("days_to_birth")]
        [JsonProperty("days_to_birth")]
        public int? DaysToBirth { get; set; }

        [BsonElement("created_datetime")]
        [JsonProperty("created_datetime")]
        public DateTime? CreatedDateTime { get; set; }

        [BsonElement("updated_datetime")]
        [JsonProperty("updated_datetime")]
        public DateTime? UpdatedDateTime { get; set; }

        [BsonElement("year_of_birth")]
        [JsonProperty("year_of_birth")]
        public int? YearOfBirth { get; set; }

        [BsonElement("days_to_death")]
        [JsonProperty("days_to_death")]
        public int? DaysToDeath { get; set; }

        [BsonElement("state")]
        [JsonProperty("state")]
        public string? State { get; set; }

        [BsonElement("year_of_death")]
        [JsonProperty("year_of_death")]
        public int? YearOfDeath { get; set; }
    }
}
