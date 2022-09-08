namespace KidneyCarcinomaRestApi.IntegrationTests.Data.Exeptions
{
    using System;

    using KidneyCarcinomaRestApi.IntegrationTests.Data.Interfaces;

    public class ApiRequestNotSuccessful : Exception
    {
        private static readonly string DefaultMessage =
            "The method returned non-successful status code.\nStatus Code: {0}\nData: {1}\nContent Type:{2}";

        public ApiRequestNotSuccessful()
        {
        }

        public ApiRequestNotSuccessful(IApiResponse response)
            : base(string.Format(DefaultMessage, (int)response.StatusCode, response.Data, response.ContentType))
        {
            this.ResponseData = response.Data;
            this.StatusCode = (int)response.StatusCode;
        }

        public ApiRequestNotSuccessful(string message, Exception inner)
            : base(message, inner)
        {
        }

        public int StatusCode { get; set; }

        public string ResponseData { get; set; }
    }
}
