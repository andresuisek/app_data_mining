import React from 'react';
import { Table } from 'antd';
import { useGetBiometricDataQuery } from '../baseApi';

const TableData = () => {
    const { data, error, isLoading } = useGetBiometricDataQuery();

    const columns = [
        {
          title: 'Date and Time',
          dataIndex: 'datetime',
          key: 'datetime',
        },
        {
          title: 'ID Number',
          dataIndex: 'id_number',
          key: 'id_number',
        },
        {
          title: 'First Name',
          dataIndex: 'first_name',
          key: 'first_name',
        },
        {
          title: 'Last Name',
          dataIndex: 'last_name',
          key: 'last_name',
        },
        {
          title: 'Phone',
          dataIndex: 'phone',
          key: 'phone',
        },
        {
          title: 'Email',
          dataIndex: 'email',
          key: 'email',
        },
        {
          title: 'Address',
          dataIndex: 'address',
          key: 'address',
        },
        {
          title: 'Company',
          dataIndex: 'company',
          key: 'company',
        },
        {
          title: 'Province',
          dataIndex: 'province',
          key: 'province',
        },
        {
          title: 'Liveness Test Result',
          dataIndex: 'life_test_result',
          key: 'life_test_result',
        },
        {
          title: 'Document Check Result',
          dataIndex: 'document_check_result',
          key: 'document_check_result',
        },
        {
          title: 'Facematch Result',
          dataIndex: 'facematch_result',
          key: 'facematch_result',
        },
        {
          title: 'Biometric Result',
          dataIndex: 'biometric_result',
          key: 'biometric_result',
          render: (text) => (
            <span style={{ backgroundColor: text === 'APROBADO' ? '#91CC75' : '#EE6666', color: 'white', display: 'block', padding: '5px' }}>
              {text}
            </span>
          ),
        },
      ];

    if (isLoading) return <div>Loading...</div>;
    if (error) return <div>Error loading data</div>;

    return (
        <Table dataSource={data} columns={columns} rowKey="id" size="small" />
    );
};

export default TableData;