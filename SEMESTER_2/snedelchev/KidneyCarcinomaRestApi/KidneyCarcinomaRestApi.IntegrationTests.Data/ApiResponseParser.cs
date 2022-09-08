namespace KidneyCarcinomaRestApi.IntegrationTests.Data
{
    using System.Xml.Linq;

    using Newtonsoft.Json.Linq;

    using KidneyCarcinomaRestApi.IntegrationTests.Data.Interfaces;

    public class ApiResponseParser : IApiResponseParser
    {
        private static IApiResponseParser instance;

        private ApiResponseParser()
        {
        }

        public static IApiResponseParser Instance => instance ?? (instance = new ApiResponseParser());

        public JObject ParseJson(string jsonData)
        {
            return JObject.Parse(jsonData);
        }

        public JArray ParseJsonArray(string jsonData)
        {
            return JArray.Parse(jsonData);
        }

        public XElement ParseXml(string xmlData)
        {
            return XElement.Parse(xmlData);
        }
    }
}
