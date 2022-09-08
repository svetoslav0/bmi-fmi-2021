namespace KidneyCarcinomaRestApi.IntegrationTests.Data.Builders
{
    using System.Net.Http;

    using KidneyCarcinomaRestApi.IntegrationTests.Data.ApiModels;
    using KidneyCarcinomaRestApi.IntegrationTests.Data.Enums;
    using KidneyCarcinomaRestApi.IntegrationTests.Data.Interfaces;

    public class ApiResponseBuilder : IApiResponseBuilder
    {
        private static IApiResponseBuilder instance;

        private ApiResponseBuilder()
        {
        }

        public static IApiResponseBuilder Instance => instance ?? (instance = new ApiResponseBuilder());

        public IApiResponse BuildApiResponseFrom(HttpResponseMessage httpResponse, IApiRequest apiRequest)
        {
            int statusCode = (int)httpResponse.StatusCode;
            string data = httpResponse.Content.ReadAsStringAsync().Result;
            ContentType contentType = apiRequest.ContentType;

            IApiResponse apiResponse = new ApiResponse(statusCode, data, contentType);
            return apiResponse;
        }
    }
}
