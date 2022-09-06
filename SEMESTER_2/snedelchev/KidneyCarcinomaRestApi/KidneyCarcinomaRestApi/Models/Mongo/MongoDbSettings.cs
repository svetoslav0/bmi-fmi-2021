namespace KidneyCarcinomaRestApi.Models.Mongo
{
    public class MongoDbSettings
    {
        public string ConnectionUri { get; set; } = null!;

        public string DatabaseName { get; set; } = null!;

        public string CasesCollectionName { get; set; } = null!;

        public string DiagnosesCollectionName { get; set; } = null!;

    }
}
