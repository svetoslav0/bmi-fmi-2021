#nullable enable
namespace KidneyCarcinomaRestApi.Models
{
    using System;
    using Microsoft.AspNetCore.Mvc;
    using MongoDB.Bson;
    using MongoDB.Bson.Serialization.Attributes;
    using Newtonsoft.Json;
    
    [BsonIgnoreExtraElements]
    public class Diagnose
    {
        [BsonId]
        [BsonRepresentation(BsonType.ObjectId)]
        [Newtonsoft.Json.JsonIgnore]
        public string? Id { get; set; }

        [BsonElement("diagnosis_id")]
        [JsonProperty("diagnosis_id")]
        [FromQuery(Name = "diagnose_id")]
        public string? DiagnoseId { get; set; }

        [BsonElement("synchronous_malignancy")]
        [JsonProperty("synchronous_malignancy")]
        [FromQuery(Name = "synchronous_malignancy")]
        public string? SynchronousMalignancy { get; set; }

        [BsonElement("ajcc_pathologic_stage")]
        [JsonProperty("ajcc_pathologic_stage")]
        [FromQuery(Name = "ajcc_pathologic_stage")]
        public string? AjccPathologicStage { get; set; }

        [BsonElement("days_to_diagnosis")]
        [JsonProperty("days_to_diagnosis")]
        [FromQuery(Name = "days_to_diagnosis")]
        public int? DaysToDiagnosis { get; set; }

        [BsonElement("created_datetime")]
        [JsonProperty("created_datetime")]
        [FromQuery(Name = "created_datetime")]
        public DateTime? CreatedDateTime { get; set; }

        [BsonElement("updated_datetime")]
        [JsonProperty("updated_datetime")]
        [FromQuery(Name = "updated_datetime")]
        public DateTime? UpdatedDateTime { get; set; }

        [BsonElement("last_known_disease_status")]
        [JsonProperty("last_known_disease_status")]
        [FromQuery(Name = "last_known_disease_status")]
        public string? LastKnownDiseaseStatus { get; set; }

        [BsonElement("tissue_or_organ_of_origin")]
        [JsonProperty("tissue_or_organ_of_origin")]
        [FromQuery(Name = "tissue_or_organ_of_origin")]
        public string? TissueOrOrganOfOrigin { get; set; }

        [BsonElement("days_to_last_follow_up")]
        [JsonProperty("days_to_last_follow_up")]
        [FromQuery(Name = "days_to_last_follow_up")]
        public int? DaysToLastFollowUp { get; set; }

        [BsonElement("age_at_diagnosis")]
        [JsonProperty("age_at_diagnosis")]
        [FromQuery(Name = "age_at_diagnosis")]
        public int? AgeAtDiagnosis { get; set; }

        [BsonElement("primary_diagnosis")]
        [JsonProperty("primary_diagnosis")]
        [FromQuery(Name = "primary_diagnosis")]
        public string? PrimaryDiagnosis { get; set; }

        [BsonElement("prior_malignancy")]
        [JsonProperty("prior_malignancy")]
        [FromQuery(Name = "prior_malignancy")]
        public string? PriorMalignancy { get; set; }

        [BsonElement("year_of_diagnosis")]
        [JsonProperty("year_of_diagnosis")]
        [FromQuery(Name = "year_of_diagnosis")]
        public int? YearOfDiagnosis { get; set; }

        [BsonElement("state")]
        [JsonProperty("state")]
        [FromQuery(Name = "state")]
        public string? State { get; set; }

        [BsonElement("prior_treatment")]
        [JsonProperty("prior_treatment")]
        [FromQuery(Name = "prior_treatment")]
        public string? PriorTreatment { get; set; }

        [BsonElement("days_to_last_known_disease_status")]
        [JsonProperty("days_to_last_known_disease_status")]
        [FromQuery(Name = "days_to_last_known_disease_status")]
        public int? DaysToLastKnownDiseaseStatus { get; set; }

        [BsonElement("ajcc_pathologic_t")]
        [JsonProperty("ajcc_pathologic_t")]
        [FromQuery(Name = "ajcc_pathologic_t")]
        public string? AjccPathologicT { get; set; }

        [BsonElement("days_to_recurrence")]
        [JsonProperty("days_to_recurrence")]
        [FromQuery(Name = "days_to_recurrence")]
        public int? DaysToRecurrence { get; set; }

        [BsonElement("morphology")]
        [JsonProperty("morphology")]
        [FromQuery(Name = "morphology")]
        public string? Morphology { get; set; }

        [BsonElement("ajcc_pathologic_n")]
        [JsonProperty("ajcc_pathologic_n")]
        [FromQuery(Name = "ajcc_pathologic_n")]
        public string? AjccPathologicN { get; set; }

        [BsonElement("ajcc_pathologic_m")]
        [JsonProperty("ajcc_pathologic_m")]
        [FromQuery(Name = "ajcc_pathologic_m")]
        public string? AjccPathologicM { get; set; }

        [BsonElement("submitter_id")]
        [JsonProperty("submitter_id")]
        [FromQuery(Name = "submitter_id")]
        public string? SubmitterId { get; set; }

        [BsonElement("classification_of_tumor")]
        [JsonProperty("classification_of_tumor")]
        [FromQuery(Name = "classification_of_tumor")]
        public string? ClassificationOfTumor { get; set; }

        [BsonElement("icd_10_code")]
        [JsonProperty("icd_10_code")]
        [FromQuery(Name = "icd_10_code")]
        public string? Icd10Code { get; set; }

        [BsonElement("site_of_resection_or_biopsy")]
        [JsonProperty("site_of_resection_or_biopsy")]
        [FromQuery(Name = "site_of_resection_or_biopsy")]
        public string? SiteOfResectionOrBiopsy { get; set; }

        [BsonElement("tumor_grade")]
        [JsonProperty("tumor_grade")]
        [FromQuery(Name = "tumor_grade")]
        public string? TumorGrade { get; set; }

        [BsonElement("progression_or_recurrence")]
        [JsonProperty("progression_or_recurrence")]
        [FromQuery(Name = "progression_or_recurrence")]
        public string? ProgressionOrRecurrence { get; set; }

        [BsonElement("treatment_ids")]
        [JsonProperty("treatment_ids")]
        [FromQuery(Name = "treatment_ids")]
        public string[]? TreatmentIds { get; set; }
    }
}
