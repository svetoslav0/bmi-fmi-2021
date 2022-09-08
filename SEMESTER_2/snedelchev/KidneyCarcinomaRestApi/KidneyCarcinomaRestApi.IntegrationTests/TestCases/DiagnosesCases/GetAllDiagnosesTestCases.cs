namespace KidneyCarcinomaRestApi.IntegrationTests.TestCases.DiagnosesCases
{
    using Microsoft.Extensions.Logging;
    using Microsoft.VisualStudio.TestTools.UnitTesting;

    using KidneyCarcinomaRestApi.IntegrationTests.Data;
    using KidneyCarcinomaRestApi.IntegrationTests.Data.ApiModels;
    using KidneyCarcinomaRestApi.IntegrationTests.Data.Builders;
    using KidneyCarcinomaRestApi.IntegrationTests.Data.Enums;
    using KidneyCarcinomaRestApi.IntegrationTests.Data.Interfaces;
    using System.Net.Http;
    using Newtonsoft.Json.Linq;

    [TestClass]
    public class GetAllDiagnosesTestCases : AbstractTestCase
    {
        private readonly IApiRequest request;

        private readonly IApiDataManager dataManager;

        private readonly IApiResponseParser responseParser;

        public GetAllDiagnosesTestCases()
        {
            this.request = new ApiRequest(AbstractTestCase.ApiUrl);
            this.request.SetContentType(ContentType.Json); // Set JSON as default

            this.dataManager = new ApiDataManager(
                ApiRequestBuilder.Instance,
                ApiResponseBuilder.Instance,
                AbstractTestCase.MillisecondsBetweenRequests);

            this.dataManager.LogLevel = LogLevel.Debug;
            this.responseParser = ApiResponseParser.Instance;
        }

        [ClassInitialize]
        public static void TestInitialize(TestContext testContext)
        {
            AbstractTestCase.AbstractClassInitialize(testContext);
        }

        [TestInitialize]
        public void TestInitialize()
        {
            this.request.UrlPath = "/diagnoses";
            this.request.Parameters = new IApiRequestParameter[] { };
        }

        [TestMethod]
        public void SomeTest()
        {
            this.request.UrlPath = "/diagnosis";
            this.request.SetContentType(ContentType.Json);
            this.request.RequestMethod = HttpMethod.Get;

            this.dataManager.RequestBuilder.BuildRequest(this.request);

            IApiResponse response = this.dataManager.SendRequest(this.request);

            Assert.IsNotNull(response);
            Assert.AreEqual(200, response.StatusCode);
            Assert.IsNotNull(response.Data);

            JObject parsedResponseData = this.responseParser.ParseJson(response.Data);
            Assert.IsNotNull(parsedResponseData["data"]);
        }
    }
}
