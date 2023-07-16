import streamlit as st
import streamlit.components.v1 as com
with open("style.css") as source:
    design = source.read()
com.html(f"""
       <style>
         {design}
       </style>


    <div class="container">
      <div class="navbar">
        <div class="logo">
          <a href="https://www.siemens.com/">
            <img
              src="https://www.siemens.com/img/svg/logo-dark-3958fff2.svg"
              alt=""
            />
          </a>
        </div>
      </div>

      <div class="intro">
        <picture
          ><!--[-->
          <source
            data-sizes="auto"
            type="image/webp"
            data-srcset="https://assets.new.siemens.com/siemens/assets/api/uuid:89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d/width:3840/quality:high/89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d.webp 3840w,https://assets.new.siemens.com/siemens/assets/api/uuid:89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d/width:2732/quality:high/89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d.webp 2732w,https://assets.new.siemens.com/siemens/assets/api/uuid:89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d/width:2224/quality:high/89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d.webp 2224w,https://assets.new.siemens.com/siemens/assets/api/uuid:89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d/width:2048/quality:high/89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d.webp 2048w,https://assets.new.siemens.com/siemens/assets/api/uuid:89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d/width:1920/quality:high/89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d.webp 1920w,https://assets.new.siemens.com/siemens/assets/api/uuid:89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d/width:1266/quality:high/89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d.webp 1266w,https://assets.new.siemens.com/siemens/assets/api/uuid:89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d/width:1125/quality:high/89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d.webp 1125w,https://assets.new.siemens.com/siemens/assets/api/uuid:89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d/width:750/quality:high/89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d.webp 750w,https://assets.new.siemens.com/siemens/assets/api/uuid:89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d/width:640/quality:high/89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d.webp 640w,https://assets.new.siemens.com/siemens/assets/api/uuid:89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d/width:320/quality:high/89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d.webp 320w,https://assets.new.siemens.com/siemens/assets/api/uuid:89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d/width:100/quality:low/89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d.webp 100w"
            data-lowsrc="https://assets.new.siemens.com/siemens/assets/api/uuid:89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d/width:100/quality:low/89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d.jpg"
            sizes="1250px"
            srcset="
              https://assets.new.siemens.com/siemens/assets/api/uuid:89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d/width:3840/quality:high/89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d.webp 3840w,
              https://assets.new.siemens.com/siemens/assets/api/uuid:89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d/width:2732/quality:high/89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d.webp 2732w,
              https://assets.new.siemens.com/siemens/assets/api/uuid:89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d/width:2224/quality:high/89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d.webp 2224w,
              https://assets.new.siemens.com/siemens/assets/api/uuid:89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d/width:2048/quality:high/89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d.webp 2048w,
              https://assets.new.siemens.com/siemens/assets/api/uuid:89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d/width:1920/quality:high/89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d.webp 1920w,
              https://assets.new.siemens.com/siemens/assets/api/uuid:89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d/width:1266/quality:high/89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d.webp 1266w,
              https://assets.new.siemens.com/siemens/assets/api/uuid:89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d/width:1125/quality:high/89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d.webp 1125w,
              https://assets.new.siemens.com/siemens/assets/api/uuid:89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d/width:750/quality:high/89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d.webp   750w,
              https://assets.new.siemens.com/siemens/assets/api/uuid:89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d/width:640/quality:high/89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d.webp   640w,
              https://assets.new.siemens.com/siemens/assets/api/uuid:89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d/width:320/quality:high/89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d.webp   320w,
              https://assets.new.siemens.com/siemens/assets/api/uuid:89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d/width:100/quality:low/89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d.webp    100w
            "
          />
          <source
            data-sizes="auto"
            data-srcset="https://assets.new.siemens.com/siemens/assets/api/uuid:89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d/width:3840/quality:high/89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d.jpg 3840w,https://assets.new.siemens.com/siemens/assets/api/uuid:89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d/width:2732/quality:high/89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d.jpg 2732w,https://assets.new.siemens.com/siemens/assets/api/uuid:89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d/width:2224/quality:high/89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d.jpg 2224w,https://assets.new.siemens.com/siemens/assets/api/uuid:89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d/width:2048/quality:high/89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d.jpg 2048w,https://assets.new.siemens.com/siemens/assets/api/uuid:89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d/width:1920/quality:high/89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d.jpg 1920w,https://assets.new.siemens.com/siemens/assets/api/uuid:89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d/width:1266/quality:high/89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d.jpg 1266w,https://assets.new.siemens.com/siemens/assets/api/uuid:89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d/width:1125/quality:high/89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d.jpg 1125w,https://assets.new.siemens.com/siemens/assets/api/uuid:89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d/width:750/quality:high/89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d.jpg 750w,https://assets.new.siemens.com/siemens/assets/api/uuid:89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d/width:640/quality:high/89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d.jpg 640w,https://assets.new.siemens.com/siemens/assets/api/uuid:89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d/width:320/quality:high/89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d.jpg 320w,https://assets.new.siemens.com/siemens/assets/api/uuid:89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d/width:100/quality:low/89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d.jpg 100w"
            data-lowsrc="https://assets.new.siemens.com/siemens/assets/api/uuid:89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d/width:100/quality:low/89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d.webp"
            sizes="1250px"
            srcset="
              https://assets.new.siemens.com/siemens/assets/api/uuid:89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d/width:3840/quality:high/89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d.jpg 3840w,
              https://assets.new.siemens.com/siemens/assets/api/uuid:89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d/width:2732/quality:high/89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d.jpg 2732w,
              https://assets.new.siemens.com/siemens/assets/api/uuid:89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d/width:2224/quality:high/89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d.jpg 2224w,
              https://assets.new.siemens.com/siemens/assets/api/uuid:89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d/width:2048/quality:high/89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d.jpg 2048w,
              https://assets.new.siemens.com/siemens/assets/api/uuid:89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d/width:1920/quality:high/89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d.jpg 1920w,
              https://assets.new.siemens.com/siemens/assets/api/uuid:89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d/width:1266/quality:high/89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d.jpg 1266w,
              https://assets.new.siemens.com/siemens/assets/api/uuid:89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d/width:1125/quality:high/89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d.jpg 1125w,
              https://assets.new.siemens.com/siemens/assets/api/uuid:89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d/width:750/quality:high/89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d.jpg   750w,
              https://assets.new.siemens.com/siemens/assets/api/uuid:89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d/width:640/quality:high/89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d.jpg   640w,
              https://assets.new.siemens.com/siemens/assets/api/uuid:89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d/width:320/quality:high/89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d.jpg   320w,
              https://assets.new.siemens.com/siemens/assets/api/uuid:89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d/width:100/quality:low/89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d.jpg    100w
            "
          />
          <!--]--><img
            data-sizes="auto"
            class="newHomeStage__imageElement blur-up lazyautosizes ls-is-cached lazyloaded"
            style=""
            data-src="https://assets.new.siemens.com/siemens/assets/api/uuid:89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d/width:100/quality:low/89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d.jpg"
            sizes="1250px"
            src="https://assets.new.siemens.com/siemens/assets/api/uuid:89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d/width:100/quality:low/89c26ff0-a4aa-4797-b8c8-21e7f4f5b56d.jpg"
          />
        </picture>
        <div class="overlay">
          <span>Siemens Smart Contract</span>
          <p>
            Discover the power of Smart Contracts and their impact on the
            industry.
          </p>
        </div>
      </div>

      <!-- Cart -->

      <div class="responsive-cart-img">
        <picture
          ><source
            data-sizes="auto"
            type="image/webp"
            data-srcset="https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:3840/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.webp 3840w,https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:2732/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.webp 2732w,https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:2224/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.webp 2224w,https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:2048/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.webp 2048w,https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:1920/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.webp 1920w,https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:1266/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.webp 1266w,https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:1125/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.webp 1125w,https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:750/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.webp 750w,https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:640/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.webp 640w,https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:320/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.webp 320w,https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:100/quality:low/3327d081-ffbe-4c01-8b2e-e26f83a964af.webp 100w"
            data-lowsrc="https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:100/quality:low/3327d081-ffbe-4c01-8b2e-e26f83a964af.jpg"
            sizes="800px"
            srcset="
              https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:3840/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.webp 3840w,
              https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:2732/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.webp 2732w,
              https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:2224/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.webp 2224w,
              https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:2048/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.webp 2048w,
              https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:1920/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.webp 1920w,
              https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:1266/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.webp 1266w,
              https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:1125/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.webp 1125w,
              https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:750/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.webp   750w,
              https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:640/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.webp   640w,
              https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:320/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.webp   320w,
              https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:100/quality:low/3327d081-ffbe-4c01-8b2e-e26f83a964af.webp    100w
            " />
          <source
            data-sizes="auto"
            data-srcset="https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:3840/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.jpg 3840w,https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:2732/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.jpg 2732w,https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:2224/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.jpg 2224w,https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:2048/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.jpg 2048w,https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:1920/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.jpg 1920w,https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:1266/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.jpg 1266w,https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:1125/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.jpg 1125w,https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:750/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.jpg 750w,https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:640/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.jpg 640w,https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:320/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.jpg 320w,https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:100/quality:low/3327d081-ffbe-4c01-8b2e-e26f83a964af.jpg 100w"
            data-lowsrc="https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:100/quality:low/3327d081-ffbe-4c01-8b2e-e26f83a964af.webp"
            sizes="800px"
            srcset="
              https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:3840/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.jpg 3840w,
              https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:2732/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.jpg 2732w,
              https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:2224/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.jpg 2224w,
              https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:2048/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.jpg 2048w,
              https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:1920/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.jpg 1920w,
              https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:1266/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.jpg 1266w,
              https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:1125/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.jpg 1125w,
              https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:750/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.jpg   750w,
              https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:640/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.jpg   640w,
              https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:320/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.jpg   320w,
              https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:100/quality:low/3327d081-ffbe-4c01-8b2e-e26f83a964af.jpg    100w
            " />
          <img
            data-sizes="auto"
            class="blur-up lazyautosizes ls-is-cached lazyloaded"
            width="4"
            height="3"
            data-src="https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:100/quality:low/3327d081-ffbe-4c01-8b2e-e26f83a964af.jpg"
            style="aspect-ratio: 4 / 3"
            sizes="800px"
            src="https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:100/quality:low/3327d081-ffbe-4c01-8b2e-e26f83a964af.jpg"
        /></picture>
      </div>
      <div class="cart">
        <div class="cart-img">
          <picture
            ><source
              data-sizes="auto"
              type="image/webp"
              data-srcset="https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:3840/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.webp 3840w,https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:2732/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.webp 2732w,https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:2224/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.webp 2224w,https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:2048/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.webp 2048w,https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:1920/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.webp 1920w,https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:1266/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.webp 1266w,https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:1125/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.webp 1125w,https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:750/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.webp 750w,https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:640/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.webp 640w,https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:320/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.webp 320w,https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:100/quality:low/3327d081-ffbe-4c01-8b2e-e26f83a964af.webp 100w"
              data-lowsrc="https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:100/quality:low/3327d081-ffbe-4c01-8b2e-e26f83a964af.jpg"
              sizes="800px"
              srcset="
                https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:3840/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.webp 3840w,
                https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:2732/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.webp 2732w,
                https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:2224/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.webp 2224w,
                https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:2048/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.webp 2048w,
                https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:1920/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.webp 1920w,
                https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:1266/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.webp 1266w,
                https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:1125/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.webp 1125w,
                https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:750/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.webp   750w,
                https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:640/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.webp   640w,
                https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:320/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.webp   320w,
                https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:100/quality:low/3327d081-ffbe-4c01-8b2e-e26f83a964af.webp    100w
              " />
            <source
              data-sizes="auto"
              data-srcset="https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:3840/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.jpg 3840w,https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:2732/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.jpg 2732w,https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:2224/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.jpg 2224w,https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:2048/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.jpg 2048w,https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:1920/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.jpg 1920w,https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:1266/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.jpg 1266w,https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:1125/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.jpg 1125w,https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:750/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.jpg 750w,https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:640/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.jpg 640w,https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:320/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.jpg 320w,https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:100/quality:low/3327d081-ffbe-4c01-8b2e-e26f83a964af.jpg 100w"
              data-lowsrc="https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:100/quality:low/3327d081-ffbe-4c01-8b2e-e26f83a964af.webp"
              sizes="800px"
              srcset="
                https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:3840/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.jpg 3840w,
                https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:2732/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.jpg 2732w,
                https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:2224/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.jpg 2224w,
                https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:2048/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.jpg 2048w,
                https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:1920/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.jpg 1920w,
                https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:1266/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.jpg 1266w,
                https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:1125/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.jpg 1125w,
                https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:750/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.jpg   750w,
                https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:640/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.jpg   640w,
                https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:320/quality:high/3327d081-ffbe-4c01-8b2e-e26f83a964af.jpg   320w,
                https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:100/quality:low/3327d081-ffbe-4c01-8b2e-e26f83a964af.jpg    100w
              " />
            <img
              data-sizes="auto"
              class="blur-up lazyautosizes ls-is-cached lazyloaded"
              width="4"
              height="3"
              data-src="https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:100/quality:low/3327d081-ffbe-4c01-8b2e-e26f83a964af.jpg"
              style="aspect-ratio: 4 / 3"
              sizes="800px"
              src="https://assets.new.siemens.com/siemens/assets/api/uuid:3327d081-ffbe-4c01-8b2e-e26f83a964af/width:100/quality:low/3327d081-ffbe-4c01-8b2e-e26f83a964af.jpg"
          /></picture>
        </div>
        <div class="cart-content">
          <h2>What Is Smart Contract ?</h2>
          <p>
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Accusamus
            doloremque quisquam perspiciatis hic atque dignissimos distinctio
            qui consequuntur quam repudiandae officiis eaque quas ratione
            ducimus corporis, ullam, eum dicta fugit laboriosam voluptatum.
            Laboriosam aspernatur minus fugiat esse in. Quisquam, labore!
          </p>
          <a href="#info">
            <p>Lets Explore</p>
          </a>
        </div>
      </div>

      <!-- INFO  -->

      <div class="info" id="info">
        <div class="info-cart">
          <div class="info-img">
            <picture
              ><source
                data-sizes="auto"
                type="image/webp"
                data-srcset="https://assets.new.siemens.com/siemens/assets/api/uuid:2a4a1d15-7b55-41dc-8cee-5b5680ffe84d/width:3840/quality:high/crop:0:0,214:0,997:0,562/2a4a1d15-7b55-41dc-8cee-5b5680ffe84d.webp 3840w,https://assets.new.siemens.com/siemens/assets/api/uuid:2a4a1d15-7b55-41dc-8cee-5b5680ffe84d/width:2732/quality:high/crop:0:0,214:0,997:0,562/2a4a1d15-7b55-41dc-8cee-5b5680ffe84d.webp 2732w,https://assets.new.siemens.com/siemens/assets/api/uuid:2a4a1d15-7b55-41dc-8cee-5b5680ffe84d/width:2224/quality:high/crop:0:0,214:0,997:0,562/2a4a1d15-7b55-41dc-8cee-5b5680ffe84d.webp 2224w,https://assets.new.siemens.com/siemens/assets/api/uuid:2a4a1d15-7b55-41dc-8cee-5b5680ffe84d/width:2048/quality:high/crop:0:0,214:0,997:0,562/2a4a1d15-7b55-41dc-8cee-5b5680ffe84d.webp 2048w,https://assets.new.siemens.com/siemens/assets/api/uuid:2a4a1d15-7b55-41dc-8cee-5b5680ffe84d/width:1920/quality:high/crop:0:0,214:0,997:0,562/2a4a1d15-7b55-41dc-8cee-5b5680ffe84d.webp 1920w,https://assets.new.siemens.com/siemens/assets/api/uuid:2a4a1d15-7b55-41dc-8cee-5b5680ffe84d/width:1266/quality:high/crop:0:0,214:0,997:0,562/2a4a1d15-7b55-41dc-8cee-5b5680ffe84d.webp 1266w,https://assets.new.siemens.com/siemens/assets/api/uuid:2a4a1d15-7b55-41dc-8cee-5b5680ffe84d/width:1125/quality:high/crop:0:0,214:0,997:0,562/2a4a1d15-7b55-41dc-8cee-5b5680ffe84d.webp 1125w,https://assets.new.siemens.com/siemens/assets/api/uuid:2a4a1d15-7b55-41dc-8cee-5b5680ffe84d/width:750/quality:high/crop:0:0,214:0,997:0,562/2a4a1d15-7b55-41dc-8cee-5b5680ffe84d.webp 750w,https://assets.new.siemens.com/siemens/assets/api/uuid:2a4a1d15-7b55-41dc-8cee-5b5680ffe84d/width:640/quality:high/crop:0:0,214:0,997:0,562/2a4a1d15-7b55-41dc-8cee-5b5680ffe84d.webp 640w,https://assets.new.siemens.com/siemens/assets/api/uuid:2a4a1d15-7b55-41dc-8cee-5b5680ffe84d/width:320/quality:high/crop:0:0,214:0,997:0,562/2a4a1d15-7b55-41dc-8cee-5b5680ffe84d.webp 320w,https://assets.new.siemens.com/siemens/assets/api/uuid:2a4a1d15-7b55-41dc-8cee-5b5680ffe84d/width:100/quality:low/crop:0:0,214:0,997:0,562/2a4a1d15-7b55-41dc-8cee-5b5680ffe84d.webp 100w"
                data-lowsrc="https://assets.new.siemens.com/siemens/assets/api/uuid:2a4a1d15-7b55-41dc-8cee-5b5680ffe84d/width:100/quality:low/crop:0:0,214:0,997:0,562/2a4a1d15-7b55-41dc-8cee-5b5680ffe84d.jpg"
                sizes="373px"
                srcset="
                  https://assets.new.siemens.com/siemens/assets/api/uuid:2a4a1d15-7b55-41dc-8cee-5b5680ffe84d/width:3840/quality:high/crop:0:0,214:0,997:0,562/2a4a1d15-7b55-41dc-8cee-5b5680ffe84d.webp 3840w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:2a4a1d15-7b55-41dc-8cee-5b5680ffe84d/width:2732/quality:high/crop:0:0,214:0,997:0,562/2a4a1d15-7b55-41dc-8cee-5b5680ffe84d.webp 2732w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:2a4a1d15-7b55-41dc-8cee-5b5680ffe84d/width:2224/quality:high/crop:0:0,214:0,997:0,562/2a4a1d15-7b55-41dc-8cee-5b5680ffe84d.webp 2224w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:2a4a1d15-7b55-41dc-8cee-5b5680ffe84d/width:2048/quality:high/crop:0:0,214:0,997:0,562/2a4a1d15-7b55-41dc-8cee-5b5680ffe84d.webp 2048w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:2a4a1d15-7b55-41dc-8cee-5b5680ffe84d/width:1920/quality:high/crop:0:0,214:0,997:0,562/2a4a1d15-7b55-41dc-8cee-5b5680ffe84d.webp 1920w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:2a4a1d15-7b55-41dc-8cee-5b5680ffe84d/width:1266/quality:high/crop:0:0,214:0,997:0,562/2a4a1d15-7b55-41dc-8cee-5b5680ffe84d.webp 1266w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:2a4a1d15-7b55-41dc-8cee-5b5680ffe84d/width:1125/quality:high/crop:0:0,214:0,997:0,562/2a4a1d15-7b55-41dc-8cee-5b5680ffe84d.webp 1125w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:2a4a1d15-7b55-41dc-8cee-5b5680ffe84d/width:750/quality:high/crop:0:0,214:0,997:0,562/2a4a1d15-7b55-41dc-8cee-5b5680ffe84d.webp   750w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:2a4a1d15-7b55-41dc-8cee-5b5680ffe84d/width:640/quality:high/crop:0:0,214:0,997:0,562/2a4a1d15-7b55-41dc-8cee-5b5680ffe84d.webp   640w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:2a4a1d15-7b55-41dc-8cee-5b5680ffe84d/width:320/quality:high/crop:0:0,214:0,997:0,562/2a4a1d15-7b55-41dc-8cee-5b5680ffe84d.webp   320w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:2a4a1d15-7b55-41dc-8cee-5b5680ffe84d/width:100/quality:low/crop:0:0,214:0,997:0,562/2a4a1d15-7b55-41dc-8cee-5b5680ffe84d.webp    100w
                " />
              <source
                data-sizes="auto"
                data-srcset="https://assets.new.siemens.com/siemens/assets/api/uuid:2a4a1d15-7b55-41dc-8cee-5b5680ffe84d/width:3840/quality:high/crop:0:0,214:0,997:0,562/2a4a1d15-7b55-41dc-8cee-5b5680ffe84d.jpg 3840w,https://assets.new.siemens.com/siemens/assets/api/uuid:2a4a1d15-7b55-41dc-8cee-5b5680ffe84d/width:2732/quality:high/crop:0:0,214:0,997:0,562/2a4a1d15-7b55-41dc-8cee-5b5680ffe84d.jpg 2732w,https://assets.new.siemens.com/siemens/assets/api/uuid:2a4a1d15-7b55-41dc-8cee-5b5680ffe84d/width:2224/quality:high/crop:0:0,214:0,997:0,562/2a4a1d15-7b55-41dc-8cee-5b5680ffe84d.jpg 2224w,https://assets.new.siemens.com/siemens/assets/api/uuid:2a4a1d15-7b55-41dc-8cee-5b5680ffe84d/width:2048/quality:high/crop:0:0,214:0,997:0,562/2a4a1d15-7b55-41dc-8cee-5b5680ffe84d.jpg 2048w,https://assets.new.siemens.com/siemens/assets/api/uuid:2a4a1d15-7b55-41dc-8cee-5b5680ffe84d/width:1920/quality:high/crop:0:0,214:0,997:0,562/2a4a1d15-7b55-41dc-8cee-5b5680ffe84d.jpg 1920w,https://assets.new.siemens.com/siemens/assets/api/uuid:2a4a1d15-7b55-41dc-8cee-5b5680ffe84d/width:1266/quality:high/crop:0:0,214:0,997:0,562/2a4a1d15-7b55-41dc-8cee-5b5680ffe84d.jpg 1266w,https://assets.new.siemens.com/siemens/assets/api/uuid:2a4a1d15-7b55-41dc-8cee-5b5680ffe84d/width:1125/quality:high/crop:0:0,214:0,997:0,562/2a4a1d15-7b55-41dc-8cee-5b5680ffe84d.jpg 1125w,https://assets.new.siemens.com/siemens/assets/api/uuid:2a4a1d15-7b55-41dc-8cee-5b5680ffe84d/width:750/quality:high/crop:0:0,214:0,997:0,562/2a4a1d15-7b55-41dc-8cee-5b5680ffe84d.jpg 750w,https://assets.new.siemens.com/siemens/assets/api/uuid:2a4a1d15-7b55-41dc-8cee-5b5680ffe84d/width:640/quality:high/crop:0:0,214:0,997:0,562/2a4a1d15-7b55-41dc-8cee-5b5680ffe84d.jpg 640w,https://assets.new.siemens.com/siemens/assets/api/uuid:2a4a1d15-7b55-41dc-8cee-5b5680ffe84d/width:320/quality:high/crop:0:0,214:0,997:0,562/2a4a1d15-7b55-41dc-8cee-5b5680ffe84d.jpg 320w,https://assets.new.siemens.com/siemens/assets/api/uuid:2a4a1d15-7b55-41dc-8cee-5b5680ffe84d/width:100/quality:low/crop:0:0,214:0,997:0,562/2a4a1d15-7b55-41dc-8cee-5b5680ffe84d.jpg 100w"
                data-lowsrc="https://assets.new.siemens.com/siemens/assets/api/uuid:2a4a1d15-7b55-41dc-8cee-5b5680ffe84d/width:100/quality:low/crop:0:0,214:0,997:0,562/2a4a1d15-7b55-41dc-8cee-5b5680ffe84d.webp"
                sizes="373px"
                srcset="
                  https://assets.new.siemens.com/siemens/assets/api/uuid:2a4a1d15-7b55-41dc-8cee-5b5680ffe84d/width:3840/quality:high/crop:0:0,214:0,997:0,562/2a4a1d15-7b55-41dc-8cee-5b5680ffe84d.jpg 3840w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:2a4a1d15-7b55-41dc-8cee-5b5680ffe84d/width:2732/quality:high/crop:0:0,214:0,997:0,562/2a4a1d15-7b55-41dc-8cee-5b5680ffe84d.jpg 2732w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:2a4a1d15-7b55-41dc-8cee-5b5680ffe84d/width:2224/quality:high/crop:0:0,214:0,997:0,562/2a4a1d15-7b55-41dc-8cee-5b5680ffe84d.jpg 2224w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:2a4a1d15-7b55-41dc-8cee-5b5680ffe84d/width:2048/quality:high/crop:0:0,214:0,997:0,562/2a4a1d15-7b55-41dc-8cee-5b5680ffe84d.jpg 2048w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:2a4a1d15-7b55-41dc-8cee-5b5680ffe84d/width:1920/quality:high/crop:0:0,214:0,997:0,562/2a4a1d15-7b55-41dc-8cee-5b5680ffe84d.jpg 1920w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:2a4a1d15-7b55-41dc-8cee-5b5680ffe84d/width:1266/quality:high/crop:0:0,214:0,997:0,562/2a4a1d15-7b55-41dc-8cee-5b5680ffe84d.jpg 1266w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:2a4a1d15-7b55-41dc-8cee-5b5680ffe84d/width:1125/quality:high/crop:0:0,214:0,997:0,562/2a4a1d15-7b55-41dc-8cee-5b5680ffe84d.jpg 1125w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:2a4a1d15-7b55-41dc-8cee-5b5680ffe84d/width:750/quality:high/crop:0:0,214:0,997:0,562/2a4a1d15-7b55-41dc-8cee-5b5680ffe84d.jpg   750w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:2a4a1d15-7b55-41dc-8cee-5b5680ffe84d/width:640/quality:high/crop:0:0,214:0,997:0,562/2a4a1d15-7b55-41dc-8cee-5b5680ffe84d.jpg   640w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:2a4a1d15-7b55-41dc-8cee-5b5680ffe84d/width:320/quality:high/crop:0:0,214:0,997:0,562/2a4a1d15-7b55-41dc-8cee-5b5680ffe84d.jpg   320w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:2a4a1d15-7b55-41dc-8cee-5b5680ffe84d/width:100/quality:low/crop:0:0,214:0,997:0,562/2a4a1d15-7b55-41dc-8cee-5b5680ffe84d.jpg    100w
                " />
              <img
                data-sizes="auto"
                alt=""
                title=""
                class="blur-up lazyautosizes lazyloaded"
                width="16"
                height="9"
                data-src="https://assets.new.siemens.com/siemens/assets/api/uuid:2a4a1d15-7b55-41dc-8cee-5b5680ffe84d/width:100/quality:low/crop:0:0,214:0,997:0,562/2a4a1d15-7b55-41dc-8cee-5b5680ffe84d.jpg"
                style="aspect-ratio: 16 / 9"
                sizes="373px"
                src="https://assets.new.siemens.com/siemens/assets/api/uuid:2a4a1d15-7b55-41dc-8cee-5b5680ffe84d/width:100/quality:low/crop:0:0,214:0,997:0,562/2a4a1d15-7b55-41dc-8cee-5b5680ffe84d.jpg"
            /></picture>
          </div>
          <div class="info-content">
            <span>Keyword Detection</span>

            <p>
              Keyword detection is a project that aims to identify specific
              words or phrases within a given text or dataset.By utilizing
              natural language processing techniques, keyword detection enables
              the extraction of relevant information and the categorization of
              content based on specific keywords.
            </p>
          </div>
        </div>
        <div class="info-cart">
          <div class="info-img-responsive">
            <picture
              ><source
                data-sizes="auto"
                type="image/webp"
                data-srcset="https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:3840/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.webp 3840w,https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:2732/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.webp 2732w,https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:2224/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.webp 2224w,https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:2048/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.webp 2048w,https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:1920/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.webp 1920w,https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:1266/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.webp 1266w,https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:1125/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.webp 1125w,https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:750/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.webp 750w,https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:640/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.webp 640w,https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:320/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.webp 320w,https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:100/quality:low/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.webp 100w"
                data-lowsrc="https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:100/quality:low/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.jpg"
                sizes="373px"
                srcset="
                  https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:3840/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.webp 3840w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:2732/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.webp 2732w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:2224/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.webp 2224w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:2048/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.webp 2048w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:1920/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.webp 1920w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:1266/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.webp 1266w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:1125/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.webp 1125w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:750/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.webp   750w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:640/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.webp   640w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:320/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.webp   320w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:100/quality:low/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.webp    100w
                " />
              <source
                data-sizes="auto"
                data-srcset="https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:3840/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.jpg 3840w,https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:2732/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.jpg 2732w,https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:2224/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.jpg 2224w,https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:2048/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.jpg 2048w,https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:1920/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.jpg 1920w,https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:1266/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.jpg 1266w,https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:1125/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.jpg 1125w,https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:750/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.jpg 750w,https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:640/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.jpg 640w,https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:320/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.jpg 320w,https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:100/quality:low/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.jpg 100w"
                data-lowsrc="https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:100/quality:low/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.webp"
                sizes="373px"
                srcset="
                  https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:3840/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.jpg 3840w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:2732/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.jpg 2732w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:2224/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.jpg 2224w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:2048/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.jpg 2048w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:1920/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.jpg 1920w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:1266/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.jpg 1266w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:1125/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.jpg 1125w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:750/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.jpg   750w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:640/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.jpg   640w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:320/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.jpg   320w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:100/quality:low/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.jpg    100w
                " />
              <img
                data-sizes="auto"
                alt=""
                title=""
                class="blur-up lazyautosizes lazyloaded"
                width="16"
                height="9"
                data-src="https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:100/quality:low/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.jpg"
                style="aspect-ratio: 16 / 9"
                sizes="373px"
                src="https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:100/quality:low/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.jpg"
            /></picture>
          </div>
          <div class="info-content">
            <span>Conract Summary</span>
            <p>
              Contract summary analysis is a project that focuses on extracting
              key information and insights from contract documents. Using
              techniques like natural language processing and machine learning,
              contract summary projects aim to automatically summarize contract
              terms, clauses, and important details.
            </p>
          </div>
          <div class="info-img info-image-hide">
            <picture
              ><source
                data-sizes="auto"
                type="image/webp"
                data-srcset="https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:3840/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.webp 3840w,https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:2732/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.webp 2732w,https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:2224/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.webp 2224w,https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:2048/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.webp 2048w,https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:1920/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.webp 1920w,https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:1266/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.webp 1266w,https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:1125/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.webp 1125w,https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:750/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.webp 750w,https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:640/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.webp 640w,https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:320/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.webp 320w,https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:100/quality:low/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.webp 100w"
                data-lowsrc="https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:100/quality:low/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.jpg"
                sizes="373px"
                srcset="
                  https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:3840/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.webp 3840w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:2732/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.webp 2732w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:2224/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.webp 2224w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:2048/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.webp 2048w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:1920/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.webp 1920w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:1266/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.webp 1266w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:1125/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.webp 1125w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:750/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.webp   750w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:640/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.webp   640w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:320/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.webp   320w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:100/quality:low/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.webp    100w
                " />
              <source
                data-sizes="auto"
                data-srcset="https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:3840/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.jpg 3840w,https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:2732/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.jpg 2732w,https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:2224/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.jpg 2224w,https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:2048/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.jpg 2048w,https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:1920/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.jpg 1920w,https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:1266/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.jpg 1266w,https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:1125/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.jpg 1125w,https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:750/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.jpg 750w,https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:640/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.jpg 640w,https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:320/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.jpg 320w,https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:100/quality:low/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.jpg 100w"
                data-lowsrc="https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:100/quality:low/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.webp"
                sizes="373px"
                srcset="
                  https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:3840/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.jpg 3840w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:2732/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.jpg 2732w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:2224/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.jpg 2224w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:2048/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.jpg 2048w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:1920/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.jpg 1920w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:1266/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.jpg 1266w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:1125/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.jpg 1125w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:750/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.jpg   750w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:640/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.jpg   640w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:320/quality:high/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.jpg   320w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:100/quality:low/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.jpg    100w
                " />
              <img
                data-sizes="auto"
                alt=""
                title=""
                class="blur-up lazyautosizes lazyloaded"
                width="16"
                height="9"
                data-src="https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:100/quality:low/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.jpg"
                style="aspect-ratio: 16 / 9"
                sizes="373px"
                src="https://assets.new.siemens.com/siemens/assets/api/uuid:b817c409-32f1-43b3-9846-e8774483fe0f/width:100/quality:low/crop:0:0,208:0,997:0,562/b817c409-32f1-43b3-9846-e8774483fe0f.jpg"
            /></picture>
          </div>
        </div>
        <div class="info-cart">
          <div class="info-img">
            <picture
              ><source
                data-sizes="auto"
                type="image/webp"
                data-srcset="https://assets.new.siemens.com/siemens/assets/api/uuid:47b50940-a582-431b-93db-5660b8820b7e/width:3840/quality:high/crop:0:0,216:0,997:0,562/47b50940-a582-431b-93db-5660b8820b7e.webp 3840w,https://assets.new.siemens.com/siemens/assets/api/uuid:47b50940-a582-431b-93db-5660b8820b7e/width:2732/quality:high/crop:0:0,216:0,997:0,562/47b50940-a582-431b-93db-5660b8820b7e.webp 2732w,https://assets.new.siemens.com/siemens/assets/api/uuid:47b50940-a582-431b-93db-5660b8820b7e/width:2224/quality:high/crop:0:0,216:0,997:0,562/47b50940-a582-431b-93db-5660b8820b7e.webp 2224w,https://assets.new.siemens.com/siemens/assets/api/uuid:47b50940-a582-431b-93db-5660b8820b7e/width:2048/quality:high/crop:0:0,216:0,997:0,562/47b50940-a582-431b-93db-5660b8820b7e.webp 2048w,https://assets.new.siemens.com/siemens/assets/api/uuid:47b50940-a582-431b-93db-5660b8820b7e/width:1920/quality:high/crop:0:0,216:0,997:0,562/47b50940-a582-431b-93db-5660b8820b7e.webp 1920w,https://assets.new.siemens.com/siemens/assets/api/uuid:47b50940-a582-431b-93db-5660b8820b7e/width:1266/quality:high/crop:0:0,216:0,997:0,562/47b50940-a582-431b-93db-5660b8820b7e.webp 1266w,https://assets.new.siemens.com/siemens/assets/api/uuid:47b50940-a582-431b-93db-5660b8820b7e/width:1125/quality:high/crop:0:0,216:0,997:0,562/47b50940-a582-431b-93db-5660b8820b7e.webp 1125w,https://assets.new.siemens.com/siemens/assets/api/uuid:47b50940-a582-431b-93db-5660b8820b7e/width:750/quality:high/crop:0:0,216:0,997:0,562/47b50940-a582-431b-93db-5660b8820b7e.webp 750w,https://assets.new.siemens.com/siemens/assets/api/uuid:47b50940-a582-431b-93db-5660b8820b7e/width:640/quality:high/crop:0:0,216:0,997:0,562/47b50940-a582-431b-93db-5660b8820b7e.webp 640w,https://assets.new.siemens.com/siemens/assets/api/uuid:47b50940-a582-431b-93db-5660b8820b7e/width:320/quality:high/crop:0:0,216:0,997:0,562/47b50940-a582-431b-93db-5660b8820b7e.webp 320w,https://assets.new.siemens.com/siemens/assets/api/uuid:47b50940-a582-431b-93db-5660b8820b7e/width:100/quality:low/crop:0:0,216:0,997:0,562/47b50940-a582-431b-93db-5660b8820b7e.webp 100w"
                data-lowsrc="https://assets.new.siemens.com/siemens/assets/api/uuid:47b50940-a582-431b-93db-5660b8820b7e/width:100/quality:low/crop:0:0,216:0,997:0,562/47b50940-a582-431b-93db-5660b8820b7e.jpg"
                sizes="373px"
                srcset="
                  https://assets.new.siemens.com/siemens/assets/api/uuid:47b50940-a582-431b-93db-5660b8820b7e/width:3840/quality:high/crop:0:0,216:0,997:0,562/47b50940-a582-431b-93db-5660b8820b7e.webp 3840w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:47b50940-a582-431b-93db-5660b8820b7e/width:2732/quality:high/crop:0:0,216:0,997:0,562/47b50940-a582-431b-93db-5660b8820b7e.webp 2732w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:47b50940-a582-431b-93db-5660b8820b7e/width:2224/quality:high/crop:0:0,216:0,997:0,562/47b50940-a582-431b-93db-5660b8820b7e.webp 2224w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:47b50940-a582-431b-93db-5660b8820b7e/width:2048/quality:high/crop:0:0,216:0,997:0,562/47b50940-a582-431b-93db-5660b8820b7e.webp 2048w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:47b50940-a582-431b-93db-5660b8820b7e/width:1920/quality:high/crop:0:0,216:0,997:0,562/47b50940-a582-431b-93db-5660b8820b7e.webp 1920w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:47b50940-a582-431b-93db-5660b8820b7e/width:1266/quality:high/crop:0:0,216:0,997:0,562/47b50940-a582-431b-93db-5660b8820b7e.webp 1266w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:47b50940-a582-431b-93db-5660b8820b7e/width:1125/quality:high/crop:0:0,216:0,997:0,562/47b50940-a582-431b-93db-5660b8820b7e.webp 1125w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:47b50940-a582-431b-93db-5660b8820b7e/width:750/quality:high/crop:0:0,216:0,997:0,562/47b50940-a582-431b-93db-5660b8820b7e.webp   750w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:47b50940-a582-431b-93db-5660b8820b7e/width:640/quality:high/crop:0:0,216:0,997:0,562/47b50940-a582-431b-93db-5660b8820b7e.webp   640w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:47b50940-a582-431b-93db-5660b8820b7e/width:320/quality:high/crop:0:0,216:0,997:0,562/47b50940-a582-431b-93db-5660b8820b7e.webp   320w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:47b50940-a582-431b-93db-5660b8820b7e/width:100/quality:low/crop:0:0,216:0,997:0,562/47b50940-a582-431b-93db-5660b8820b7e.webp    100w
                " />
              <source
                data-sizes="auto"
                data-srcset="https://assets.new.siemens.com/siemens/assets/api/uuid:47b50940-a582-431b-93db-5660b8820b7e/width:3840/quality:high/crop:0:0,216:0,997:0,562/47b50940-a582-431b-93db-5660b8820b7e.jpg 3840w,https://assets.new.siemens.com/siemens/assets/api/uuid:47b50940-a582-431b-93db-5660b8820b7e/width:2732/quality:high/crop:0:0,216:0,997:0,562/47b50940-a582-431b-93db-5660b8820b7e.jpg 2732w,https://assets.new.siemens.com/siemens/assets/api/uuid:47b50940-a582-431b-93db-5660b8820b7e/width:2224/quality:high/crop:0:0,216:0,997:0,562/47b50940-a582-431b-93db-5660b8820b7e.jpg 2224w,https://assets.new.siemens.com/siemens/assets/api/uuid:47b50940-a582-431b-93db-5660b8820b7e/width:2048/quality:high/crop:0:0,216:0,997:0,562/47b50940-a582-431b-93db-5660b8820b7e.jpg 2048w,https://assets.new.siemens.com/siemens/assets/api/uuid:47b50940-a582-431b-93db-5660b8820b7e/width:1920/quality:high/crop:0:0,216:0,997:0,562/47b50940-a582-431b-93db-5660b8820b7e.jpg 1920w,https://assets.new.siemens.com/siemens/assets/api/uuid:47b50940-a582-431b-93db-5660b8820b7e/width:1266/quality:high/crop:0:0,216:0,997:0,562/47b50940-a582-431b-93db-5660b8820b7e.jpg 1266w,https://assets.new.siemens.com/siemens/assets/api/uuid:47b50940-a582-431b-93db-5660b8820b7e/width:1125/quality:high/crop:0:0,216:0,997:0,562/47b50940-a582-431b-93db-5660b8820b7e.jpg 1125w,https://assets.new.siemens.com/siemens/assets/api/uuid:47b50940-a582-431b-93db-5660b8820b7e/width:750/quality:high/crop:0:0,216:0,997:0,562/47b50940-a582-431b-93db-5660b8820b7e.jpg 750w,https://assets.new.siemens.com/siemens/assets/api/uuid:47b50940-a582-431b-93db-5660b8820b7e/width:640/quality:high/crop:0:0,216:0,997:0,562/47b50940-a582-431b-93db-5660b8820b7e.jpg 640w,https://assets.new.siemens.com/siemens/assets/api/uuid:47b50940-a582-431b-93db-5660b8820b7e/width:320/quality:high/crop:0:0,216:0,997:0,562/47b50940-a582-431b-93db-5660b8820b7e.jpg 320w,https://assets.new.siemens.com/siemens/assets/api/uuid:47b50940-a582-431b-93db-5660b8820b7e/width:100/quality:low/crop:0:0,216:0,997:0,562/47b50940-a582-431b-93db-5660b8820b7e.jpg 100w"
                data-lowsrc="https://assets.new.siemens.com/siemens/assets/api/uuid:47b50940-a582-431b-93db-5660b8820b7e/width:100/quality:low/crop:0:0,216:0,997:0,562/47b50940-a582-431b-93db-5660b8820b7e.webp"
                sizes="373px"
                srcset="
                  https://assets.new.siemens.com/siemens/assets/api/uuid:47b50940-a582-431b-93db-5660b8820b7e/width:3840/quality:high/crop:0:0,216:0,997:0,562/47b50940-a582-431b-93db-5660b8820b7e.jpg 3840w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:47b50940-a582-431b-93db-5660b8820b7e/width:2732/quality:high/crop:0:0,216:0,997:0,562/47b50940-a582-431b-93db-5660b8820b7e.jpg 2732w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:47b50940-a582-431b-93db-5660b8820b7e/width:2224/quality:high/crop:0:0,216:0,997:0,562/47b50940-a582-431b-93db-5660b8820b7e.jpg 2224w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:47b50940-a582-431b-93db-5660b8820b7e/width:2048/quality:high/crop:0:0,216:0,997:0,562/47b50940-a582-431b-93db-5660b8820b7e.jpg 2048w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:47b50940-a582-431b-93db-5660b8820b7e/width:1920/quality:high/crop:0:0,216:0,997:0,562/47b50940-a582-431b-93db-5660b8820b7e.jpg 1920w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:47b50940-a582-431b-93db-5660b8820b7e/width:1266/quality:high/crop:0:0,216:0,997:0,562/47b50940-a582-431b-93db-5660b8820b7e.jpg 1266w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:47b50940-a582-431b-93db-5660b8820b7e/width:1125/quality:high/crop:0:0,216:0,997:0,562/47b50940-a582-431b-93db-5660b8820b7e.jpg 1125w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:47b50940-a582-431b-93db-5660b8820b7e/width:750/quality:high/crop:0:0,216:0,997:0,562/47b50940-a582-431b-93db-5660b8820b7e.jpg   750w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:47b50940-a582-431b-93db-5660b8820b7e/width:640/quality:high/crop:0:0,216:0,997:0,562/47b50940-a582-431b-93db-5660b8820b7e.jpg   640w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:47b50940-a582-431b-93db-5660b8820b7e/width:320/quality:high/crop:0:0,216:0,997:0,562/47b50940-a582-431b-93db-5660b8820b7e.jpg   320w,
                  https://assets.new.siemens.com/siemens/assets/api/uuid:47b50940-a582-431b-93db-5660b8820b7e/width:100/quality:low/crop:0:0,216:0,997:0,562/47b50940-a582-431b-93db-5660b8820b7e.jpg    100w
                " />
              <img
                data-sizes="auto"
                alt=""
                title=""
                class="blur-up lazyautosizes lazyloaded"
                width="16"
                height="9"
                data-src="https://assets.new.siemens.com/siemens/assets/api/uuid:47b50940-a582-431b-93db-5660b8820b7e/width:100/quality:low/crop:0:0,216:0,997:0,562/47b50940-a582-431b-93db-5660b8820b7e.jpg"
                style="aspect-ratio: 16 / 9"
                sizes="373px"
                src="https://assets.new.siemens.com/siemens/assets/api/uuid:47b50940-a582-431b-93db-5660b8820b7e/width:100/quality:low/crop:0:0,216:0,997:0,562/47b50940-a582-431b-93db-5660b8820b7e.jpg"
            /></picture>
          </div>
          <div class="info-content">
            <span>Contract Analysis</span>
            <p>
              Contract analysis involves the systematic examination of contract
              documents to understand their terms, conditions, and legal
              implications. Through the use of technology and AI-powered tools,
              contract analysis projects aim to automate the process of
              reviewing and extracting key information from contracts, such as
              parties involved, obligations, and rights.
            </p>
          </div>
        </div>
      </div>
      <!-- Footer -->
      <div class="footer">
        <a href="https://www.siemens.com/" class="footer-link">
          <p>Siemens</p>
        </a>

        <span class="footer-year">
          <p>
            © Siemens 1996 -
            <span id="currentYear"></span>
          </p>
          <script>
            var currentYear = new Date().getFullYear();
            document.getElementById("currentYear").textContent = currentYear;
          </script>
        </span>
        <a
          href="https://www.siemens.com/us/en/company/about/contact-us.html"
          class="contact-us"
          >Contact Us</a
        >
      </div>
    </div>
  



""" , width=1920 , height=3240)