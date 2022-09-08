namespace KidneyCarcinomaRestApi.IntegrationTests.Data.Extensions
{
    using System;
    using System.Collections.Specialized;
    using System.Web;

    using KidneyCarcinomaRestApi.IntegrationTests.Data.Enums;
    using KidneyCarcinomaRestApi.IntegrationTests.Data.Interfaces;

    public static class HttpExtensions
    {
        public static Uri FromParameters(this Uri uri, IApiRequestParameter[] parameters)
        {
            NameValueCollection httpValueCollection = HttpUtility.ParseQueryString(uri.Query);

            foreach (IApiRequestParameter param in parameters)
            {
                if (param.Type == ApiRequestParameterType.Query)
                {
                    httpValueCollection.Remove(param.Key);
                    httpValueCollection.Add(param.Key, param.Value);
                }
            }

            UriBuilder ub = new UriBuilder(uri);
            ub.Query = httpValueCollection.ToString();

            return ub.Uri;
        }
    }
}
