namespace KidneyCarcinomaRestApi.IntegrationTests.Data.Interfaces
{
    using System.Net.Http;
    using KidneyCarcinomaRestApi.IntegrationTests.Data.Enums;

    public interface IApiRequest : IContent
    {
        string BaseUrl { get; }

        string UrlPath { get; set; }

        HttpMethod RequestMethod { get; set; }

        IApiRequestParameter[] Parameters { get; set; }

        void SetContentType(ContentType contentType);

        void SetRequestMessage(HttpRequestMessage requestMessage);

        string GetBodyParametersAsString();

        string GetRequestUrl();

        HttpResponseMessage Execute();
    }
}
