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
        [BindProperty(Name = "diagnose_id", SupportsGet = true)]
        public string? DiagnoseId { get; set; }

        [BsonElement("synchronous_malignancy")]
        [JsonProperty("synchronous_malignancy")]
        [BindProperty(Name = "synchronous_malignancy", SupportsGet = true)]
        public string? SynchronousMalignancy { get; set; }

        [BsonElement("ajcc_pathologic_stage")]
        [JsonProperty("ajcc_pathologic_stage")]
        [BindProperty(Name = "ajcc_pathologic_stage", SupportsGet = true)]
        public string? AjccPathologicStage { get; set; }

        [BsonElement("days_to_diagnosis")]
        [JsonProperty("days_to_diagnosis")]
        [BindProperty(Name = "days_to_diagnosis", SupportsGet = true)]
        public int? DaysToDiagnosis { get; set; }

        [BsonElement("created_datetime")]
        [JsonProperty("created_datetime")]
        [BindProperty(Name = "created_datetime", SupportsGet = true)]
        public DateTime? CreatedDateTime { get; set; }

        [BsonElement("updated_datetime")]
        [JsonProperty("updated_datetime")]
        [BindProperty(Name = "updated_datetime", SupportsGet = true)]
        public DateTime? UpdatedDateTime { get; set; }

        [BsonElement("last_known_disease_status")]
        [JsonProperty("last_known_disease_status")]
        [BindProperty(Name = "last_known_disease_status", SupportsGet = true)]
        public string? LastKnownDiseaseStatus { get; set; }

        [BsonElement("tissue_or_organ_of_origin")]
        [JsonProperty("tissue_or_organ_of_origin")]
        [BindProperty(Name = "tissue_or_organ_of_origin", SupportsGet = true)]
        public string? TissueOrOrganOfOrigin { get; set; }

        [BsonElement("days_to_last_follow_up")]
        [JsonProperty("days_to_last_follow_up")]
        [BindProperty(Name = "days_to_last_follow_up", SupportsGet = true)]
        public int? DaysToLastFollowUp { get; set; }

        [BsonElement("age_at_diagnosis")]
        [JsonProperty("age_at_diagnosis")]
        [BindProperty(Name = "age_at_diagnosis", SupportsGet = true)]
        public int? AgeAtDiagnosis { get; set; }

        [BsonElement("primary_diagnosis")]
        [JsonProperty("primary_diagnosis")]
        [BindProperty(Name = "primary_diagnosis", SupportsGet = true)]
        public string? PrimaryDiagnosis { get; set; }

        [BsonElement("prior_malignancy")]
        [JsonProperty("prior_malignancy")]
        [BindProperty(Name = "prior_malignancy", SupportsGet = true)]
        public string? PriorMalignancy { get; set; }

        [BsonElement("year_of_diagnosis")]
        [JsonProperty("year_of_diagnosis")]
        [BindProperty(Name = "year_of_diagnosis", SupportsGet = true)]
        public int? YearOfDiagnosis { get; set; }

        [BsonElement("state")]
        [JsonProperty("state")]
        [BindProperty(Name = "state", SupportsGet = true)]
        public string? State { get; set; }

        [BsonElement("prior_treatment")]
        [JsonProperty("prior_treatment")]
        [BindProperty(Name = "prior_treatment", SupportsGet = true)]
        public string? PriorTreatment { get; set; }

        [BsonElement("days_to_last_known_disease_status")]
        [JsonProperty("days_to_last_known_disease_status")]
        [BindProperty(Name = "days_to_last_known_disease_status", SupportsGet = true)]
        public int? DaysToLastKnownDiseaseStatus { get; set; }

        [BsonElement("ajcc_pathologic_t")]
        [JsonProperty("ajcc_pathologic_t")]
        [BindProperty(Name = "ajcc_pathologic_t", SupportsGet = true)]
        public string? AjccPathologicT { get; set; }

        [BsonElement("days_to_recurrence")]
        [JsonProperty("days_to_recurrence")]
        [BindProperty(Name = "days_to_recurrence", SupportsGet = true)]
        public int? DaysToRecurrence { get; set; }

        [BsonElement("morphology")]
        [JsonProperty("morphology")]
        [BindProperty(Name = "morphology", SupportsGet = true)]
        public string? Morphology { get; set; }

        [BsonElement("ajcc_pathologic_n")]
        [JsonProperty("ajcc_pathologic_n")]
        [BindProperty(Name = "ajcc_pathologic_n", SupportsGet = true)]
        public string? AjccPathologicN { get; set; }

        [BsonElement("ajcc_pathologic_m")]
        [JsonProperty("ajcc_pathologic_m")]
        [BindProperty(Name = "ajcc_pathologic_m", SupportsGet = true)]
        public string? AjccPathologicM { get; set; }

        [BsonElement("submitter_id")]
        [JsonProperty("submitter_id")]
        [BindProperty(Name = "submitter_id", SupportsGet = true)]
        public string? SubmitterId { get; set; }

        [BsonElement("classification_of_tumor")]
        [JsonProperty("classification_of_tumor")]
        [BindProperty(Name = "classification_of_tumor", SupportsGet = true)]
        public string? ClassificationOfTumor { get; set; }

        [BsonElement("icd_10_code")]
        [JsonProperty("icd_10_code")]
        [BindProperty(Name = "icd_10_code", SupportsGet = true)]
        public string? Icd10Code { get; set; }

        [BsonElement("site_of_resection_or_biopsy")]
        [JsonProperty("site_of_resection_or_biopsy")]
        [BindProperty(Name = "site_of_resection_or_biopsy", SupportsGet = true)]
        public string? SiteOfResectionOrBiopsy { get; set; }

        [BsonElement("tumor_grade")]
        [JsonProperty("tumor_grade")]
        [BindProperty(Name = "tumor_grade", SupportsGet = true)]
        public string? TumorGrade { get; set; }

        [BsonElement("progression_or_recurrence")]
        [JsonProperty("progression_or_recurrence")]
        [BindProperty(Name = "progression_or_recurrence", SupportsGet = true)]
        public string? ProgressionOrRecurrence { get; set; }

        [BsonElement("treatment_ids")]
        [JsonProperty("treatment_ids")]
        [BindProperty(Name = "treatment_ids", SupportsGet = true)]
        public string[]? TreatmentIds { get; set; }
    }
}
