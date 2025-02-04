import React from 'react';
import { Descriptions } from 'antd';

const Step1 = () => {
    const items = [
        {
            key: '1',
            label: 'University',
            children: 'UISEK',
        },
        {
          key: '2',
          label: 'Student',
          children: 'Andres Ontiveros',
        },
        {
          key: '3',
          label: 'Semester',
          children: '6to',
        },
        {
          key: '4',
          label: 'Subject',
          children: 'Data Mining',
        },
        {
            key: '5',
            label: 'Teacher',
            span: 2,
            children: 'Phd. Julián Galindo',
        },
        {
            key: '6',
            label: 'Description',
            // span: 3,
            children: 'This project consists of predicting the level of severity of a detected vulnerability.',
        }                                
      ];

    return (
        <>
            <br />
            <Descriptions bordered layout="vertical" items={items} />
        </>
    );
};

export default Step1;