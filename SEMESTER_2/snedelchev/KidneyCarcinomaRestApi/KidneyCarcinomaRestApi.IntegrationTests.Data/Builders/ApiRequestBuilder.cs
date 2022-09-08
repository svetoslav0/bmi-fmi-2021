namespace KidneyCarcinomaRestApi.IntegrationTests.Data.Builders
{
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Net.Http;

    using KidneyCarcinomaRestApi.IntegrationTests.Data.ApiModels;
    using KidneyCarcinomaRestApi.IntegrationTests.Data.Enums;
    using KidneyCarcinomaRestApi.IntegrationTests.Data.Extensions;
    using KidneyCarcinomaRestApi.IntegrationTests.Data.Interfaces;

    public class ApiRequestBuilder : IApiRequestBuilder
    {
        private static IApiRequestBuilder instance;

        private ApiRequestBuilder()
        {
        }

        public static IApiRequestBuilder Instance => instance ?? (instance = new ApiRequestBuilder());

        public void BuildRequest(IApiRequest apiRequest)
        {
            switch (apiRequest.RequestMethod.Method)
            {
                case "GET":
                    this.BuildGetRequest(apiRequest);
                    break;
                case "POST":
                case "PATCH":
                case "DELETE":
                    this.BuildPostPatchDeleteRequest(apiRequest);
                    break;
                default:
                    throw new NotImplementedException($"HTTP Method \"{apiRequest.RequestMethod}\" is not implemented.");
            }
        }

        private void BuildPostPatchDeleteRequest(IApiRequest apiRequest)
        {
            string requestUrl = this.BuildPostPatchDeleteRequestUrl(apiRequest);
            HttpRequestMessage requestMessage = new HttpRequestMessage(apiRequest.RequestMethod, requestUrl);
            requestMessage.Content = this.BuildRequestContent(apiRequest.Parameters);

            apiRequest.SetRequestMessage(requestMessage);
        }

        private FormUrlEncodedContent BuildRequestContent(IApiRequestParameter[] parameters)
        {
            Dictionary<string, string> requestParams = new Dictionary<string, string>();

            foreach (IApiRequestParameter param in parameters)
            {
                if (param.Type == ApiRequestParameterType.Body)
                {
                    requestParams.Add(param.Key, param.Value);
                }
            }

            FormUrlEncodedContent content = new FormUrlEncodedContent(requestParams);
            return content;
        }

        private string BuildPostPatchDeleteRequestUrl(IApiRequest apiRequest)
        {
            IApiRequestParameter[] queryParams = this.GetQueryParameters(apiRequest);
            Uri resultUri = new Uri($"{apiRequest.BaseUrl}/{apiRequest.UrlPath}").FromParameters(queryParams);

            return resultUri.ToString();
        }

        private void BuildGetRequest(IApiRequest apiRequest)
        {
            string requestUrl = this.BuildGetRequestUrl(apiRequest);
            HttpRequestMessage getRequestMessage = new HttpRequestMessage(HttpMethod.Get, requestUrl);
            apiRequest.SetRequestMessage(getRequestMessage);
        }

        private string BuildGetRequestUrl(IApiRequest apiRequest)
        {
            IApiRequestParameter[] queryParams = this.GetQueryParameters(apiRequest);
            Uri resultUri = new Uri($"{apiRequest.BaseUrl}/{apiRequest.UrlPath}").FromParameters(queryParams);

            return resultUri.ToString();
        }

        private string GetContentTypeAsString(ContentType contentType)
        {
            return contentType.ToString().ToLower();
        }

        private IApiRequestParameter[] GetQueryParameters(IApiRequest apiRequest)
        {
            IApiRequestParameter[] requiredParameters = this.GetRequiredQueryParameters(apiRequest);
            requiredParameters = requiredParameters
                .Concat(apiRequest.Parameters)
                .Where(p => p.Type == ApiRequestParameterType.Query)
                .ToArray();

            return requiredParameters;
        }

        private IApiRequestParameter[] GetRequiredQueryParameters(IApiRequest apiRequest)
        {
            return new ApiRequestParameter[]
            {
                new ApiRequestParameter("format", this.GetContentTypeAsString(apiRequest.ContentType), ApiRequestParameterType.Query)
            };
        }
    }
}
