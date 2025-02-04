// api.js
import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';

export const baseApi = createApi({
  reducerPath: 'baseApi',
  // baseQuery: fetchBaseQuery({ baseUrl: 'https://app-data-analysis-sqvh.onrender.com/api/',  retry: 0}),
  baseQuery: fetchBaseQuery({ baseUrl: 'http://127.0.0.1:8000/api/',  retry: 0}),
  endpoints: (builder) => ({
    getSeverityCount: builder.query({
      query: () => 'severity-count/'
    }),
    getScatterData: builder.query({
      query: () => 'severity-vs-cvss-chart/'
    }),
    sendFormData: builder.mutation({
      query: (formData) => ({
        url: 'prediction/',
        method: 'POST',
        body: formData,
      }),
    }),
    uploadCSV: builder.mutation({
      query: (file) => ({
        url: 'upload-csv/',
        method: 'POST',
        body: file,
        extraOptions: { maxRetries: 1 },
        // headers: {
        //   'Content-Type': 'multipart/form-data',
        // },
      }),
    }),
    getBiometricData: builder.query({
      query: () => 'biometric-data/'
    }),
    getBiometricLifeTestResults: builder.query({
      query: () => 'biometric-life-test-results/'
    }),
    getBiometricFacematchResults: builder.query({
      query: () => 'biometric-facematch-results/'
    }),
    getBiometricResults: builder.query({
      query: () => 'biometric-results/'
    }),
  })
});

export const { useGetSeverityCountQuery, useGetScatterDataQuery, useUploadCSVMutation, useSendFormDataMutation, useGetBiometricDataQuery, useGetBiometricLifeTestResultsQuery, 
  useGetBiometricFacematchResultsQuery, useGetBiometricResultsQuery  } = baseApi;