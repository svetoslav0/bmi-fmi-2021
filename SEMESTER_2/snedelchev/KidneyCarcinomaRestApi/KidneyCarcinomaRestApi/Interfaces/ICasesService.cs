namespace KidneyCarcinomaRestApi.Interfaces
{
    using System.Collections.Generic;

    using KidneyCarcinomaRestApi.Models;
    using KidneyCarcinomaRestApi.Models.Parameters;

    public interface ICasesService
    {
        public List<Case> GetAllCases(AbstractParameters parameters);

        public long GetAllCasesCount();
    }
}