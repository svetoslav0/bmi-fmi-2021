namespace KidneyCarcinomaRestApi.IntegrationTests.Data.ApiModels
{
    using System;
    using System.Net.Http;

    using KidneyCarcinomaRestApi.IntegrationTests.Data.Enums;
    using KidneyCarcinomaRestApi.IntegrationTests.Data.Interfaces;

    public class ApiRequest : IApiRequest
    {
        private static HttpClient client = new HttpClient();

        private string baseUrl;
        private string urlPath;

        private IApiRequestParameter[] parameters;
        private HttpRequestMessage requestMessage;

        public ApiRequest(HttpClient client)
        {
            ApiRequest.client = client ?? throw new ArgumentNullException($"Parameter of type HttpClient can not be null!");
        }

        public ApiRequest(string url)
        {
            this.BaseUrl = url;
            this.Parameters = new IApiRequestParameter[] { };
        }

        public string BaseUrl
        {
            get => this.baseUrl.TrimEnd('/');
            private set => this.baseUrl = !string.IsNullOrEmpty(value)
                ? value
                : throw new ArgumentOutOfRangeException(message: "BaseUrl cannot be null or empty", paramName: "URL");
        }

        public virtual string UrlPath
        {
            get => this.urlPath.TrimStart('/');
            set => this.urlPath = value
                                  ?? throw new ArgumentOutOfRangeException(
                                          message: $"{nameof(this.urlPath)} cannot be null or empty",
                                          paramName: nameof(this.urlPath));
        }

        public virtual HttpMethod RequestMethod { get; set; }

        public virtual IApiRequestParameter[] Parameters
        {
            get => this.parameters;
            set => this.parameters = value
                   ?? throw new ArgumentOutOfRangeException(
                       message: "Parameters cannot be null",
                       paramName: nameof(this.parameters));
        }

        public ContentType ContentType
        {
            get;
            private set;
        }

        public HttpResponseMessage Execute()
        {
            if (this.requestMessage == null)
            {
                throw new NullReferenceException(
                    $"You have to build the request first by using {nameof(IApiRequestBuilder)}!");
            }

            HttpResponseMessage response = ApiRequest.client.SendAsync(this.requestMessage).Result;
            return response;
        }

        public string GetRequestUrl()
        {
            return this.requestMessage.RequestUri.ToString();
        }

        public string GetBodyParametersAsString()
        {
            return this.requestMessage.Content.ReadAsStringAsync().Result;
        }

        public void SetRequestMessage(HttpRequestMessage msg)
        {
            this.requestMessage = msg;
        }

        public void SetContentType(ContentType contentType)
        {
            this.ContentType = contentType;
        }
    }
}
