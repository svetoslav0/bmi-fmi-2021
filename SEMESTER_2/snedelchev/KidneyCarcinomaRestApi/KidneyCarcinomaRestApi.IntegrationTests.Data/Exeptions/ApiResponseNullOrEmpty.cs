namespace KidneyCarcinomaRestApi.IntegrationTests.Data.Exeptions
{
    using System;

    using KidneyCarcinomaRestApi.IntegrationTests.Data.Interfaces;

    public class ApiResponseNullOrEmpty : Exception
    {
        private static readonly string DefaultMessage =
            "Response can't be null or empty.\nStatus Code: {0}\nContent Type:{1}";

        public ApiResponseNullOrEmpty()
        {
        }

        public ApiResponseNullOrEmpty(IApiResponse response)
            : base(string.Format(DefaultMessage, response.StatusCode, response.ContentType))
        {
        }

        public ApiResponseNullOrEmpty(string message, Exception inner)
            : base(message, inner)
        {
        }
    }
}
