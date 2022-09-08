namespace KidneyCarcinomaRestApi.IntegrationTests.Data.Interfaces
{
    using Microsoft.Extensions.Logging;

    public interface IApiDataManager
    {
        int MillisecondsBetweenRequests { get; set; }

        LogLevel LogLevel { get; set; }

        IApiRequestBuilder RequestBuilder { get; set; }

        IApiResponseBuilder ResponseBuilder { get; set; }

        IApiResponse SendRequest(IApiRequest apiRequest);
    }
}
