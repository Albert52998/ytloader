import './App.css';
import HeadBan from "./components/headban";
import Help from './components/Help';
import {Route, Switch} from 'react-router-dom';

function App() {
  return (
      <div className="App">
        <Switch>
          <Route path='/' exact component={HeadBan} />
          <Route path='/help/' exact component={Help} />
        </Switch>
      </div>
  );
}

export default App;
