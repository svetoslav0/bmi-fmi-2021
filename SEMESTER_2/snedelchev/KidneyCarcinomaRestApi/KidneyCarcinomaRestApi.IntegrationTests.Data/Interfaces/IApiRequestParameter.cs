namespace KidneyCarcinomaRestApi.IntegrationTests.Data.Interfaces
{
    using KidneyCarcinomaRestApi.IntegrationTests.Data.Enums;

    public interface IApiRequestParameter
    {
        string Key { get; set; }

        string Value { get; set; }

        ApiRequestParameterType Type { get; set; }
    }
}
