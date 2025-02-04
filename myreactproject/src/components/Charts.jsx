import React from 'react';
import { useGetBiometricResultsQuery } from '../baseApi';
import { Col, Row, Typography } from 'antd';
import ReactECharts from 'echarts-for-react';

const { Title } = Typography;

const Charts = () => {
    const { data: dataBiometricResults } = useGetBiometricResultsQuery();

    const colors = ['#91CC75', '#EE6666'];

    const optionBiometricResults = (data) => ({
        tooltip: {
          trigger: 'item'
        },
        legend: {
          orient: 'horizontal',
          bottom: '0%',
          left: 'center'
        },
        series: [
          {
            name: 'Results',
            type: 'pie',
            radius: '50%',
            center: ['50%', '50%'],
            data: data.map((item, index) => ({
              value: item.count,
              name: item.biometric_result,
              itemStyle: {
                color: colors[index % colors.length],
              },
            })),
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            },
            label: {
              show: true,
              formatter: '{b}: {c} ({d}%)'
            }
          }
        ]
    });

    return (
        <Row justify="center" gutter={[16, 16]}>
            <Col span={24}>
                <Title level={3} style={{ textAlign: 'center' }}>Biometric Results</Title>
                {dataBiometricResults && <ReactECharts option={optionBiometricResults(dataBiometricResults)} style={{ height: 400 }} />}
            </Col>
        </Row>
    );
};

export default Charts;