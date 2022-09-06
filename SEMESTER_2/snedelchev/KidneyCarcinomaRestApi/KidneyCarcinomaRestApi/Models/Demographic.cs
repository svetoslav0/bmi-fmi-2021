namespace KidneyCarcinomaRestApi.Models
{
    using System;

    public class Demographic
    {
        public string DemographicId { get; set; }

        public string Race { get; set; }

        public string Gender { get; set; }

        public string Ethnicity { get; set; }

        public string VitalStatus { get; set; }

        public int AgeAtIndex { get; set; }

        public string SubmitterId { get; set; }

        public int DaysToBirth { get; set; }

        public DateTime CreatedDateTime { get; set; }

        public DateTime UpdatedDateTime { get; set; }

        public int YearOfBirth { get; set; }

        public int DaysToDeath { get; set; }

        public string State { get; set; }

        public int YearOfDeath { get; set; }
    }
}
