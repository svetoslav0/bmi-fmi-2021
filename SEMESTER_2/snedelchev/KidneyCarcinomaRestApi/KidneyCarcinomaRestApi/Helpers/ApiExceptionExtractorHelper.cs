namespace KidneyCarcinomaRestApi.Helpers
{
    using System;
    using System.Reflection;
    using Microsoft.AspNetCore.Mvc;

    using KidneyCarcinomaRestApi.Exceptions;

    public class ApiExceptionExtractorHelper
    {
        private static int maxInnerExceptionDepth = 3;

        public static string GetExceptionPropByNameWithReflection(ActionContext obj, string name)
        {
            string propValue = null;
            Type contextType = obj.GetType();
            PropertyInfo exceptionProp = contextType.GetProperty("Exception");
            
            if (exceptionProp != null)
            {
                var exceptionObj = exceptionProp.GetValue(obj);

                if (exceptionObj != null)
                {
                    propValue = RecursiveExceptionPropValueExtract(exceptionObj, name);
                }
            }

            return propValue;
        }
        
        private static string RecursiveExceptionPropValueExtract(object exceptionObj, string name, int currentDepth = 0)
        {
            if (exceptionObj == null || 
                exceptionObj.GetType() == typeof(Exception) ||
                currentDepth > maxInnerExceptionDepth)
            {
                return string.Empty;
            }
            
            PropertyInfo parameterProp = exceptionObj.GetType().GetProperty(name);

            return parameterProp != null
                ? parameterProp.GetValue(exceptionObj)?.ToString()
                : RecursiveExceptionPropValueExtract(((Exception)exceptionObj).InnerException, name, ++currentDepth);
        }
    }
}