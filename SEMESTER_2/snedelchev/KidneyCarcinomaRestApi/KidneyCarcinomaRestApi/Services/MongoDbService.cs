namespace KidneyCarcinomaRestApi.Services
{
    using System.Collections.Generic;
    using System.Linq;
    using System.Threading.Tasks;
    using Microsoft.Extensions.Options;

    using KidneyCarcinomaRestApi.Models;
    using KidneyCarcinomaRestApi.Models.Mongo;
    using KidneyCarcinomaRestApi.Models.Parameters;

    using MongoDB.Bson;
    using MongoDB.Driver;

    public class MongoDbService
    {
        private readonly IMongoCollection<Case> casesCollection;
        private readonly IMongoCollection<Diagnose> diagnosesCollection;

        public MongoDbService(IOptions<MongoDbSettings> mongoDbSettings)
        {
            MongoClient client = new MongoClient(mongoDbSettings.Value.ConnectionUri);
            IMongoDatabase database = client.GetDatabase(mongoDbSettings.Value.DatabaseName);
            this.casesCollection = database.GetCollection<Case>(mongoDbSettings.Value.CasesCollectionName);
            this.diagnosesCollection = database.GetCollection<Diagnose>(mongoDbSettings.Value.DiagnosesCollectionName);
        }

        public async Task<List<Diagnose>> GetAllDiagnoses(AbstractParameters parameters)
        {
            List<Diagnose> result = await this.diagnosesCollection
                .Find(new BsonDocument())
                .Limit(parameters.Limit)
                .Skip(parameters.Offset)
                .ToListAsync();

            return result;
        }

        public long GetAllDiagnosesCount()
        {
            long result = this.diagnosesCollection.CountDocuments(new BsonDocument());

            return result;
        }

        public Diagnose GetDiagnoseById(string id)
        {
            FilterDefinition<Diagnose> filter = Builders<Diagnose>.Filter.Eq("diagnosis_id", id);

            Diagnose result = this.diagnosesCollection
                .Find(filter)
                .ToList()
                .FirstOrDefault();

            return result;
        }
    }
}
