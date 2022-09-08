namespace KidneyCarcinomaRestApi.Services
{
    using System.Collections.Generic;
    using KidneyCarcinomaRestApi.Interfaces;
    using KidneyCarcinomaRestApi.Models;
    using KidneyCarcinomaRestApi.Models.Parameters;

    using MongoDB.Bson;
    using MongoDB.Driver;

    public class CasesService : ICasesService
    {
        private readonly IMongoCollection<Case> casesCollection;

        public CasesService(IMongoCollection<Case> casesCollection)
        {
            this.casesCollection = casesCollection;
        }
        
        public List<Case> GetAllCases(AbstractParameters parameters)
        {
            List<Case> result = this.casesCollection
                .Find(new BsonDocument())
                .Limit(parameters.Limit)
                .Skip(parameters.Offset)
                .ToList();

            return result;
        }

        public long GetAllCasesCount()
        {
            long result = this.casesCollection.CountDocuments(new BsonDocument());

            return result;
        }
    }
}