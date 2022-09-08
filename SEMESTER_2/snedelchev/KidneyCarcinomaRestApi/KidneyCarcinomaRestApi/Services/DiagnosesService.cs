#nullable enable
namespace KidneyCarcinomaRestApi.Services
{
    using System.Collections.Generic;
    using System.Linq;
    using System.Reflection;
    using KidneyCarcinomaRestApi.Exceptions;
    using KidneyCarcinomaRestApi.Interfaces;
    using KidneyCarcinomaRestApi.Models;
    using KidneyCarcinomaRestApi.Models.Parameters;

    using MongoDB.Bson;
    using MongoDB.Bson.Serialization.Attributes;
    using MongoDB.Driver;

    public class DiagnosesService : IDiagnosesService
    {
        private readonly IMongoCollection<Diagnose> diagnosesCollection;

        public DiagnosesService(IMongoCollection<Diagnose> diagnosesCollection)
        {
            this.diagnosesCollection = diagnosesCollection;
        }
        
        public List<Diagnose> GetAllDiagnoses(AbstractParameters parameters, Diagnose searchParameters)
        {
            FilterDefinition<Diagnose>[] filterDefinition = this.BuildSearchFilter(searchParameters);
            FilterDefinition<Diagnose> filter = Builders<Diagnose>.Filter.Or(filterDefinition);

            this.diagnosesCollection.Find(new BsonDocument());
            
            List<Diagnose> result = this.diagnosesCollection
                .Find(filterDefinition.Length == 0 ? new BsonDocument() : filter)
                .Limit(parameters.Limit)
                .Skip(parameters.Offset)
                .ToList();

            return result;
        }

        public long GetAllDiagnosesCount(Diagnose searchParameters)
        {
            FilterDefinition<Diagnose>[] filterDefinition = this.BuildSearchFilter(searchParameters);
            FilterDefinition<Diagnose> filter = Builders<Diagnose>.Filter.Or(filterDefinition);

            long result = this.diagnosesCollection
                .CountDocuments(filterDefinition.Length == 0 ? new BsonDocument() : filter);

            return result;
        }

        public Diagnose GetDiagnoseById(string id)
        {
            FilterDefinition<Diagnose> filter = Builders<Diagnose>.Filter.Eq("diagnosis_id", id);

            Diagnose result = this.diagnosesCollection
                .Find(filter)
                .ToList()
                .FirstOrDefault()!;

            if (result == null)
            {
                throw new ApiNotFoundException("Diagnose with such ID could not be found", "id");
            }

            return result;
        }

        private FilterDefinition<Diagnose>[] BuildSearchFilter(Diagnose searchParameters)
        {
            List<KeyValuePair<string, object>> parameters = new List<KeyValuePair<string, object>>();
            
            PropertyInfo[] properties = searchParameters.GetType().GetProperties();
            foreach (PropertyInfo propertyInfo in properties)
            {
                object? value = propertyInfo.GetValue(searchParameters);

                if (value != null)
                {
                    string name = propertyInfo.Name;
                    object? attributeObj = typeof(Diagnose)
                        .GetProperty(name)
                        ?.GetCustomAttributes(false)
                        .ToDictionary(x => x.GetType().Name, x => x)
                        .FirstOrDefault(x => x.Key == "BsonElementAttribute")
                        .Value;

                    BsonElementAttribute bsonAttribute = (BsonElementAttribute)attributeObj!;
                    string paramName = bsonAttribute.ElementName;
                    
                    parameters.Add(new KeyValuePair<string, object>(paramName, value));
                }
            }

            FilterDefinition<Diagnose>[] filters = new FilterDefinition<Diagnose>[parameters.Count];
            for (int i = 0; i < parameters.Count; i++)
            {
                string currentParam = parameters[i].Key;
                object? currentValue = parameters[i].Value;
                filters[i] = Builders<Diagnose>.Filter.Eq(currentParam, currentValue);
            }

            return filters;
        }
    }
}