namespace KidneyCarcinomaRestApi.IntegrationTests.Data.Interfaces
{
    using Newtonsoft.Json.Linq;
    using System.Xml.Linq;

    public interface IApiResponseParser
    {
        JObject ParseJson(string jsonData);

        JArray ParseJsonArray(string jsonData);

        XElement ParseXml(string xmlData);
    }
}
