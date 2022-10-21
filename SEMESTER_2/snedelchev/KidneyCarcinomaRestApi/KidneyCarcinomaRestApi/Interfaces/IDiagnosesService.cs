namespace KidneyCarcinomaRestApi.Interfaces
{
    using System.Collections.Generic;
    using KidneyCarcinomaRestApi.Models;
    using KidneyCarcinomaRestApi.Models.Parameters;

    public interface IDiagnosesService
    {
        public List<Diagnose> GetAllDiagnoses(AbstractParameters parameters, Diagnose searchParameters);

        public long GetAllDiagnosesCount(Diagnose searchParameters);

        public Diagnose GetDiagnoseById(string id);

        public void Save(Diagnose diagnose);
    }
}