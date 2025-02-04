import React, {useState, useRef} from 'react';
import { Breadcrumb, Layout, Menu, theme, Col, Row, Divider, Tour, Typography, Tooltip, Button, Flex, Alert } from 'antd';
import { InfoCircleOutlined, PrinterOutlined } from '@ant-design/icons';
// import Humidity from './components/Humidity';
// import Temperature from './components/Temperature';
import Charts from './components/Charts'

import UisekLogo from './images/LOGO-UISEK-web-387x143-1.png';
import Step1 from './components/Step1';
import Step2 from './components/Step2';
import TableData from './components/TableData';

// import UploadData from './components/UploadData';
import VulnerabilityForm from './components/VulnerabilityForm ';
import Step3 from './components/Step3';

const { Header, Content, Footer } = Layout;
const { Title } = Typography;


const items = [{
  key:  1,
  label: 'Home',
}];

const App = () => {
  const {
    token: { colorBgContainer, borderRadiusLG },
  } = theme.useToken();

  const ref = useRef(null);
  const [open, setOpen] = useState(true);

  const steps = [
    {
      title: 'Welcome, this is my Final project',
      description: <Step1 />,
      target: null,
    },
    {
      title: 'Description of the fields',
      description: <Step3 />,
      target: null,
    },
    {
      title: 'Project architecture',
      description: <Step2 />,     
    },
    // {
    //   title: 'Top',
    //   description: 'On the top of target.',
    //   placement: 'top',
    //   target: () => ref.current,
    // },
  ];
  return (
    <Layout>
      <Header
        style={{
          display: 'flex',
          alignItems: 'center',
        }}
      >
        <div className="demo-logo" style={{marginRight: '30px', marginTop: '20px', width: '150px'}}>
          <img src={UisekLogo} alt='logo' style={{width: '100%'}}></img>
        </div>
        <Menu
          theme="dark"
          mode="horizontal"
          defaultSelectedKeys={['1']}
          items={items}
          style={{
            flex: 1,
            minWidth: 0,
          }}
        />
      </Header>
      
      <Content
        style={{
          padding: '0 48px',
        }}
      >
        <Breadcrumb
          style={{
            margin: '16px 0',
          }}
        >
          <Breadcrumb.Item>Home</Breadcrumb.Item>
          <Breadcrumb.Item>App</Breadcrumb.Item>
        </Breadcrumb>
        
        <div
          style={{
            background: colorBgContainer,
            minHeight: 1000,
            padding: 24,
            borderRadius: borderRadiusLG,
          }}
        >
          <Alert
            message="Biometric data obtained from WhatsApp in Ecuador."
            type="info"
            showIcon
            style={{ marginBottom: 24 }}
          />
           <Row>
              <Col span={12}>
                <Charts />
              </Col>
              <Col span={12}>
                <VulnerabilityForm />
              </Col>
              <Divider type="horizontal" />
            </Row>

            <Flex justify={'space-between'} align={'center'}>
              <Title level={3} style={{'marginTop': 0}}>Historical Data</Title>
              <div>
                <Tooltip title="Print PDF">
                  <Button 
                    onClick={() => window.print()} 
                    shape="circle" 
                    icon={<PrinterOutlined />} 
                    style={{ marginRight: '8px' }}
                  />
                </Tooltip>
                <Tooltip title="Information">
                  <Button onClick={() => setOpen(true)} shape="circle" icon={<InfoCircleOutlined />} />
                </Tooltip>
              </div>
            </Flex>            
            
            <TableData />
              
        </div>
      </Content>
      <Footer
        style={{
          textAlign: 'center',
        }}
      >
      </Footer>
      <Tour style={{ width: 'auto'}} open={open} onClose={() => setOpen(false)} steps={steps} />
    </Layout>
  );
};
export default App;