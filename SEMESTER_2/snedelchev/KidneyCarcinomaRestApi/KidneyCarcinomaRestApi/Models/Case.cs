namespace KidneyCarcinomaRestApi.Models
{
    public class Case
    {
        public string CaseId { get; set; }

        public Demographic Demographic { get; set; }

        public string[] ExposureIds { get; set; }

        public string[] DiagnosesIds { get; set; }
    }
}
