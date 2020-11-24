import React from 'react';
import Header from './Header';
import './main.css';
import './fonts/fonts.css';

export default function Help() {
  return (
      <>
        <Header />

        <div className="help-block">
          <div className="container">
            <p className="help">
              Lorem ipsum dolor sit amet, consectetur adipisicing elit. A ab aperiam aspernatur assumenda blanditiis consequuntur, delectus facere, inventore maxime molestias odit officia omnis quo repellat repudiandae sunt veniam voluptates voluptatum?
            </p>
            <p className="help">
              Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ab amet dicta ipsa labore molestiae officiis possimus quaerat ratione. Aliquam assumenda corporis deleniti dolorem esse fugiat officiis provident rerum sit veniam!
            </p>
            <p className="help">
              Lorem ipsum dolor sit amet, consectetur adipisicing elit. Distinctio explicabo facere facilis quis repudiandae? Ab, amet autem dicta doloremque necessitatibus nobis numquam quos recusandae sequi voluptate. Fugit, incidunt vel. Nostrum?
            </p>
            <p className="help">
              Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus debitis dicta dignissimos ducimus ex exercitationem facere iste minima natus, nobis odit pariatur praesentium quis repellat repellendus totam vitae voluptatibus? Unde.
            </p>
            <p className="help">
              Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cupiditate et id ipsam nam nihil odio praesentium reiciendis repellat? Adipisci beatae culpa dignissimos est eum quas saepe totam veritatis vitae, voluptas.
            </p>
          </div>
        </div>
      </>
  );
}