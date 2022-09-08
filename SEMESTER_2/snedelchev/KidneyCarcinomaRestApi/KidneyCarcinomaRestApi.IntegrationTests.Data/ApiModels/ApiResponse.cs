namespace KidneyCarcinomaRestApi.IntegrationTests.Data.ApiModels
{
    using KidneyCarcinomaRestApi.IntegrationTests.Data.Enums;
    using KidneyCarcinomaRestApi.IntegrationTests.Data.Interfaces;

    public class ApiResponse : IApiResponse
    {
        private int statusCode;
        private string data;

        public ApiResponse(int statusCode, string data, ContentType contentType)
        {
            this.StatusCode = statusCode;
            this.Data = data;
            this.ContentType = contentType;
        }

        public int StatusCode
        {
            get => this.statusCode;
            private set => this.statusCode = value;
        }

        public string Data
        {
            get => this.data;
            private set => this.data = value;
        }

        public virtual ContentType ContentType { get; private set; }
    }
}
