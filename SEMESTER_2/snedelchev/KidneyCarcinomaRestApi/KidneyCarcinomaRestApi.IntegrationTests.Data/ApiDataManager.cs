namespace KidneyCarcinomaRestApi.IntegrationTests.Data
{
    using System;
    using System.Net.Http;
    using System.Threading;
    using System.Linq;

    using Newtonsoft.Json;
    using Microsoft.Extensions.Logging;

    using KidneyCarcinomaRestApi.IntegrationTests.Data.Interfaces;
    using KidneyCarcinomaRestApi.IntegrationTests.Data.Exeptions;
    using KidneyCarcinomaRestApi.IntegrationTests.Data.Enums;
    using KidneyCarcinomaRestApi.IntegrationTests.Data.Extensions;

    public class ApiDataManager : IApiDataManager
    {
        private IApiRequestBuilder requestBuilder;
        private IApiResponseBuilder responseBuilder;

        private int millisecondsBetweenRequests;

        public ApiDataManager(IApiRequestBuilder requestBuilder, IApiResponseBuilder responseBuilder, int millisecondsBetweenRequests = 0)
        {
            this.RequestBuilder = requestBuilder;
            this.ResponseBuilder = responseBuilder;
            this.MillisecondsBetweenRequests = millisecondsBetweenRequests;
        }

        public LogLevel LogLevel { get; set; } = LogLevel.Information;

        public IApiRequestBuilder RequestBuilder
        {
            get => this.requestBuilder;
            set => this.requestBuilder = value
                                         ?? throw new ArgumentOutOfRangeException(
                                             message: $"{nameof(this.RequestBuilder)} must not be null",
                                             paramName: nameof(this.RequestBuilder));
        }

        public IApiResponseBuilder ResponseBuilder
        {
            get => this.responseBuilder;
            set => this.responseBuilder = value
                                          ?? throw new ArgumentOutOfRangeException(
                                              message: $"{nameof(this.RequestBuilder)} must not be null",
                                              paramName: nameof(this.RequestBuilder));
        }

        public int MillisecondsBetweenRequests
        {
            get =>
                this.millisecondsBetweenRequests;

            set => this.millisecondsBetweenRequests = value >= 0
                ? value
                : throw new ArgumentOutOfRangeException(
                    message: $"{nameof(this.MillisecondsBetweenRequests)} must not be < 0",
                    paramName: nameof(this.MillisecondsBetweenRequests));
        }

        public IApiResponse SendRequest(IApiRequest apiRequest)
        {
            this.LogRequestData(apiRequest);

            this.Wait();

            this.RequestBuilder.BuildRequest(apiRequest);
            HttpResponseMessage webResponse = apiRequest.Execute();

            IApiResponse apiResponse = this.ResponseBuilder.BuildApiResponseFrom(webResponse, apiRequest);
            this.ValidateApiResponse(apiResponse);

            return apiResponse;
        }

        private void ValidateApiResponse(IApiResponse response)
        {
            if ((int)response.StatusCode >= 400)
            {
                throw new ApiRequestNotSuccessful(response);
            }

            if (string.IsNullOrEmpty(response.Data))
            {
                throw new ApiResponseNullOrEmpty(response);
            }
        }

        private void LogRequestData(IApiRequest apiRequest)
        {
            string debugString = $"Sending request:{Environment.NewLine}" +
                                 $"URL: {apiRequest.BaseUrl}/{apiRequest.UrlPath}{Environment.NewLine}";

            if (this.LogLevel == LogLevel.Debug)
            {
                debugString += $"Full URL: {apiRequest.GetRequestUrl()}\n";
            }

            if (apiRequest.Parameters.Length > 0)
            {
                debugString += this.ParseBodyParameters(apiRequest);
            }

            Console.WriteLine(debugString);
        }

        private string ParseBodyParameters(IApiRequest apiRequest)
        {
            IApiRequestParameter[] parameters = apiRequest.Parameters
                .Where(p => p.Type == ApiRequestParameterType.Body)
                .ToArray();

            string jsonString = JsonConvert.SerializeObject(
                parameters,
                Formatting.Indented,
                new RequestParametersConverter());

            return $"Body Parameters: {jsonString}";
        }

        private void Wait()
        {
            if (this.MillisecondsBetweenRequests <= 0)
            {
                return;
            }

            Console.WriteLine($"Waiting for {this.MillisecondsBetweenRequests} ms");
            Thread.Sleep(this.MillisecondsBetweenRequests);
            Console.WriteLine("Done waiting");
        }
    }
}
