namespace KidneyCarcinomaRestApi.IntegrationTests.Data.Interfaces
{
    using KidneyCarcinomaRestApi.IntegrationTests.Data.Enums;

    public interface IApiResponse : IContent
    {
        int StatusCode { get; }

        string Data { get; }

        ContentType ContentType { get; }
    }
}
