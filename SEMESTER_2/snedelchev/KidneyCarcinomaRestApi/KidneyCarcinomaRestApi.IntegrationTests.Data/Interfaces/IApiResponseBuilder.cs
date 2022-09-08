namespace KidneyCarcinomaRestApi.IntegrationTests.Data.Interfaces
{
    using System.Net.Http;

    public interface IApiResponseBuilder
    {
        IApiResponse BuildApiResponseFrom(HttpResponseMessage httpResponse, IApiRequest apiRequest);
    }
}
