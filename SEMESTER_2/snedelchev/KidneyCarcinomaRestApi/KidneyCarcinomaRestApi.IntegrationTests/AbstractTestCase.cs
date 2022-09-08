namespace KidneyCarcinomaRestApi.IntegrationTests
{
    using System;
    using System.Linq;
    
    using Microsoft.VisualStudio.TestTools.UnitTesting;

    using KidneyCarcinomaRestApi.IntegrationTests.Data.Enums;
    using KidneyCarcinomaRestApi.IntegrationTests.Constants;
    using KidneyCarcinomaRestApi.IntegrationTests.Exceptions;

    public abstract class AbstractTestCase
    {
        public static int MillisecondsBetweenRequests => 2000;

        protected static string ApiUrl { get; set; }

        protected static ApiEnvironment ApiEnvironment { get; set; }

        protected static void AbstractClassInitialize(TestContext testContext, params string[] props)
        {
            string[] requiredProperties = new string[]
            {
                TestProperties.ApiUrl,
                TestProperties.Env,
            };

            if (props.Length > 0)
            {
                requiredProperties = requiredProperties.Concat(props).ToArray();
            }

            CheckTestContextProperties(testContext, requiredProperties);

            ApiUrl = testContext.Properties[TestProperties.ApiUrl]?.ToString();
            ApiEnvironment = Enum.Parse<ApiEnvironment>(testContext.Properties[TestProperties.Env].ToString());

            // Add more fields and properties for specific needs
        }

        private static void CheckTestContextProperties(TestContext testContext, string[] includedProps)
        {
            foreach (string p in includedProps)
            {
                if (string.IsNullOrEmpty((string)testContext.Properties[p]))
                {
                    throw new MissingTestSettingsException($"Missing property {p} in test settings.");
                }
            }
        }
    }
}
