namespace KidneyCarcinomaRestApi.IntegrationTests.Data.ApiModels
{
    using KidneyCarcinomaRestApi.IntegrationTests.Data.Enums;
    using KidneyCarcinomaRestApi.IntegrationTests.Data.Interfaces;

    public class ApiRequestParameter : IApiRequestParameter
    {
        public ApiRequestParameter()
        {
        }

        public ApiRequestParameter(string key, string value, ApiRequestParameterType type = ApiRequestParameterType.Query)
        {
            this.Key = key;
            this.Value = value;
            this.Type = type;
        }

        public virtual string Key { get; set; }

        public virtual string Value { get; set; }

        public virtual ApiRequestParameterType Type { get; set; }
    }
}
