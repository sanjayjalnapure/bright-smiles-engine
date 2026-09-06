import { createFileRoute } from "@tanstack/react-router";
import { useEffect, useState } from "react";
import {
  Phone,
  MapPin,
  Clock,
  Sparkles,
  Stethoscope,
  Smile,
  ShieldCheck,
  GraduationCap,
  Award,
  Menu,
  X,
  ArrowUpRight,
  ArrowRight,
  Check,
  Timer,
  HeartHandshake,
  MessageCircle,
} from "lucide-react";

import { Reveal } from "@/components/Reveal";
import { Counter } from "@/components/Counter";
import logo from "@/assets/logo.png.asset.json";
import clinicEntrance from "@/assets/clinic-entrance.png.asset.json";
import heroClinic from "@/assets/hero-clinic.jpg";
import smileDesign from "@/assets/smile-design.jpg";
import generalDentistry from "@/assets/general-dentistry.jpg";
import cosmeticDentistry from "@/assets/cosmetic-dentistry.jpg";
import doctorPhoto from "@/assets/doctor.jpg";

export const Route = createFileRoute("/")({
  head: () => ({
    meta: [
      { title: "Dhanvantari Dental Clinic Solapur | Dr. Sanika Phadke" },
      {
        name: "description",
        content:
          "Advanced dental care in Solapur — general dentistry, smile designing and cosmetic dentistry by Dr. Sanika Phadke, B.D.S. (MUHS). Call 9168362233.",
      },
      { property: "og:title", content: "Dhanvantari Dental Clinic Solapur | Dr. Sanika Phadke" },
      {
        property: "og:description",
        content:
          "General dentistry, smile designing and cosmetic dentistry at Shete Nagar, Laxmi Peth, Solapur.",
      },
      { property: "og:type", content: "website" },
      { name: "twitter:card", content: "summary_large_image" },
    ],
  }),
  component: Home,
});

const PHONE = "9168362233";
const WHATSAPP = "https://wa.me/919168362233";
const MAP_URL = "https://maps.app.goo.gl/mwtY7YMqPcS7rMus8";

const NAV = [
  { label: "Home", href: "#home" },
  { label: "About Us", href: "#about" },
  { label: "Treatments", href: "#services" },
  { label: "Safety First", href: "#why" },
  { label: "Our Clinic", href: "#clinic" },
  { label: "Contact Us", href: "#contact" },
];

const STATS = [
  { n: 2, s: "", l: "Fellowships" },
  { n: 3, s: "", l: "Core Specialities" },
  { n: 100, s: "%", l: "Sterile Protocol" },
  { n: 1, s: ":1", l: "Doctor Attention" },
];

const SERVICES = [
  {
    title: "General Dentistry",
    image: generalDentistry,
    icon: Stethoscope,
    text: "Check-ups, scaling, tooth-coloured fillings, root canal treatment and extractions — done gently and hygienically.",
  },
  {
    title: "Smile Designing",
    image: smileDesign,
    icon: Smile,
    text: "A smile planned around your face — shape, shade and proportion balanced so the result still looks like you.",
  },
  {
    title: "Cosmetic Dentistry",
    image: cosmeticDentistry,
    icon: Sparkles,
    text: "Veneers, whitening and ceramic crowns using precise, tooth-friendly techniques for a natural finish.",
  },
  {
    title: "Painless Root Canals",
    image: heroClinic,
    icon: ShieldCheck,
    text: "Single-visit root canal therapy with modern rotary instruments and effective local anaesthesia.",
  },
];

const WHY = [
  {
    icon: HeartHandshake,
    title: "Maximum Comfort",
    text: "Calm, unhurried treatment with everything explained in plain language before it begins.",
  },
  {
    icon: Timer,
    title: "Optimal Efficiency",
    text: "Appointment-based slots so your treatment starts on time, with minimal waiting.",
  },
  {
    icon: ShieldCheck,
    title: "Uncompromising Safety",
    text: "Autoclaved instruments and single-use disposables for every single patient, every visit.",
  },
];

const EYEBROW = "text-xs font-semibold tracking-[0.28em] uppercase";

function Home() {
  const [scrolled, setScrolled] = useState(false);
  const [open, setOpen] = useState(false);

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 20);
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  return (
    <div id="home" className="min-h-screen bg-background">
      {/* Header */}
      <header
        className={`fixed inset-x-0 top-0 z-50 bg-background transition-all duration-300 ${
          scrolled ? "py-2 shadow-soft" : "py-3"
        }`}
      >
        <div className="mx-auto flex max-w-7xl items-center justify-between gap-4 px-5">
          <a href="#home" className="flex items-center gap-3">
            <img
              src={logo.url}
              alt="Dhanvantari Multispeciality Dental Clinic logo"
              width={56}
              height={56}
              className="h-12 w-12 rounded-full"
            />
            <span className="leading-tight">
              <span className="block font-display text-sm font-bold sm:text-base">Dhanvantari</span>
              <span className="block text-[0.6rem] tracking-[0.18em] text-muted-foreground uppercase sm:text-[0.65rem]">
                Multispeciality Dental Clinic
              </span>
            </span>
          </a>

          <nav className="hidden items-center gap-7 xl:flex">
            {NAV.map((n) => (
              <a
                key={n.href}
                href={n.href}
                className="relative text-sm font-medium after:absolute after:-bottom-1.5 after:left-0 after:h-0.5 after:w-full after:origin-bottom-right after:scale-x-0 after:bg-primary after:transition-transform after:duration-300 hover:text-primary hover:after:origin-bottom-left hover:after:scale-x-100"
              >
                {n.label}
              </a>
            ))}
          </nav>

          <div className="flex items-center gap-3">
            <a
              href={WHATSAPP}
              target="_blank"
              rel="noreferrer"
              aria-label="Chat on WhatsApp"
              className="hidden h-11 w-11 items-center justify-center rounded-full bg-primary text-primary-foreground transition-transform duration-300 hover:-translate-y-0.5 sm:inline-flex"
            >
              <MessageCircle className="h-5 w-5" />
            </a>
            <a
              href={`tel:${PHONE}`}
              className="btn-accent hidden items-center gap-3 rounded-full py-1.5 pr-1.5 pl-6 text-sm font-semibold md:inline-flex"
            >
              Book Appointment
              <span className="inline-flex h-9 w-9 items-center justify-center rounded-full bg-accent text-accent-foreground">
                <ArrowUpRight className="h-4 w-4" />
              </span>
            </a>
            <button aria-label="Menu" onClick={() => setOpen((v) => !v)} className="xl:hidden">
              {open ? <X className="h-7 w-7" /> : <Menu className="h-7 w-7" />}
            </button>
          </div>
        </div>

        {open && (
          <div className="mx-5 mt-3 rounded-2xl bg-card p-4 shadow-lift xl:hidden">
            {NAV.map((n) => (
              <a
                key={n.href}
                href={n.href}
                onClick={() => setOpen(false)}
                className="block border-b border-border/60 py-3 text-sm font-medium last:border-0"
              >
                {n.label}
              </a>
            ))}
            <a
              href={`tel:${PHONE}`}
              className="btn-accent mt-3 flex items-center justify-center gap-2 rounded-full px-5 py-3 text-sm font-semibold"
            >
              <Phone className="h-4 w-4" /> Book Appointment
            </a>
          </div>
        )}
      </header>

      {/* Hero */}
      <section className="relative flex min-h-[88vh] items-center overflow-hidden pt-28 pb-16">
        <img
          src={heroClinic}
          alt="Treatment room at Dhanvantari Multispeciality Dental Clinic, Solapur"
          width={1600}
          height={1104}
          className="absolute inset-0 h-full w-full object-cover"
        />
        <div aria-hidden className="surface-hero absolute inset-0" />
        <div className="relative mx-auto max-w-4xl px-5 text-center">
          <Reveal>
            <p className={`${EYEBROW} text-white/85`}>
              <Sparkles className="mr-2 inline h-3.5 w-3.5 text-primary" />
              Welcome to Dhanvantari Dental Clinic
            </p>
          </Reveal>
          <Reveal delay={120}>
            <h1 className="mt-6 text-4xl leading-[1.05] font-extrabold text-white sm:text-5xl md:text-7xl">
              Advanced Care for a{" "}
              <span className="text-primary">Brighter, Healthier</span> Smile
            </h1>
          </Reveal>
          <Reveal delay={240}>
            <p className="mx-auto mt-7 max-w-2xl text-base text-white/80 md:text-lg">
              Gentle, modern dentistry in Solapur under the care of Dr. Sanika Sudha Kiranchandra
              Phadke — general dentistry, smile designing and cosmetic dentistry in one calm clinic.
            </p>
          </Reveal>
          <Reveal delay={340}>
            <div className="mt-9 flex flex-wrap items-center justify-center gap-4">
              <a
                href={`tel:${PHONE}`}
                className="btn-accent inline-flex items-center gap-2 rounded-full px-7 py-3.5 text-sm font-semibold"
              >
                <Phone className="h-4 w-4" /> {PHONE}
              </a>
              <a
                href="#services"
                className="btn-outline-light inline-flex items-center gap-2 rounded-full px-7 py-3.5 text-sm font-semibold"
              >
                View treatments
              </a>
            </div>
          </Reveal>
          <Reveal delay={440}>
            <p className="mt-8 text-sm text-white/75">
              B.D.S. (MUHS) · Fellowship in General Dentistry · Fellowship in Smile Designing &amp;
              Cosmetic Dentistry
            </p>
          </Reveal>
        </div>
      </section>

      {/* Stats band */}
      <section className="bg-primary-deep py-12">
        <div className="mx-auto grid max-w-7xl grid-cols-2 gap-y-10 px-5 lg:grid-cols-4">
          {STATS.map((s, i) => (
            <Reveal
              key={s.l}
              delay={i * 110}
              className={`text-center ${i > 0 ? "lg:border-l lg:border-white/15" : ""}`}
            >
              <p className="font-display text-3xl font-extrabold text-primary md:text-5xl">
                <Counter to={s.n} suffix={s.s} />
              </p>
              <p className="mt-2 text-xs tracking-[0.2em] text-white/75 uppercase">{s.l}</p>
            </Reveal>
          ))}
        </div>
      </section>

      {/* About */}
      <section id="about" className="py-24 md:py-32">
        <div className="mx-auto grid max-w-7xl items-center gap-16 px-5 lg:grid-cols-2">
          <Reveal from="left">
            <div className="relative pb-16 pl-0 sm:pl-12">
              <img
                src={clinicEntrance.url}
                alt="Entrance of Dhanvantari Multispeciality Dental Clinic in Solapur"
                loading="lazy"
                width={1200}
                height={860}
                className="w-full rounded-[2rem] object-cover shadow-lift"
              />
              <img
                src={generalDentistry}
                alt="Dental treatment in progress at the clinic"
                loading="lazy"
                width={1200}
                height={1200}
                className="absolute bottom-0 left-0 hidden h-52 w-52 rounded-[1.5rem] border-4 border-background object-cover shadow-lift sm:block"
              />
              <span className="animate-float absolute -top-6 right-4 flex h-24 w-24 flex-col items-center justify-center rounded-full bg-primary text-center font-display text-xs font-bold text-primary-foreground shadow-lift">
                <span className="text-xl">3</span>
                Specialities
              </span>
            </div>
          </Reveal>

          <div>
            <Reveal>
              <p className={`${EYEBROW} text-primary`}>About the clinic</p>
              <h2 className="mt-4 text-3xl font-extrabold md:text-5xl">
                Solapur&apos;s caring centre for everyday and cosmetic dentistry
              </h2>
              <p className="mt-6 text-muted-foreground">
                Dhanvantari Multispeciality Dental Clinic sits inside Dhanvantari Nursing Home at
                Shete Nagar, Laxmi Peth. Dr. Sanika Sudha Kiranchandra Phadke, B.D.S. (MUHS), brings
                fellowship training in general dentistry and in smile designing &amp; cosmetic
                dentistry to every treatment plan.
              </p>
              <p className="mt-4 text-muted-foreground">
                From a simple cleaning to a full smile makeover, you get a proper diagnosis, honest
                options and a clear cost before anything starts — in a thoroughly sterilised,
                comfortable setting.
              </p>
            </Reveal>
            <div className="mt-8 grid gap-4 sm:grid-cols-2">
              {[
                "B.D.S. (MUHS)",
                "Fellowship in General Dentistry",
                "Fellowship in Smile Designing",
                "Fellowship in Cosmetic Dentistry",
              ].map((q, i) => (
                <Reveal key={q} delay={i * 100}>
                  <div className="flex items-center gap-3 text-sm font-semibold">
                    <span className="inline-flex h-7 w-7 shrink-0 items-center justify-center rounded-full bg-primary text-primary-foreground">
                      <Check className="h-4 w-4" />
                    </span>
                    {q}
                  </div>
                </Reveal>
              ))}
            </div>
            <Reveal delay={420}>
              <a
                href="#contact"
                className="btn-accent mt-10 inline-flex items-center gap-3 rounded-full py-1.5 pr-1.5 pl-6 text-sm font-semibold"
              >
                Visit the clinic
                <span className="inline-flex h-9 w-9 items-center justify-center rounded-full bg-accent text-accent-foreground">
                  <ArrowUpRight className="h-4 w-4" />
                </span>
              </a>
            </Reveal>
          </div>
        </div>
      </section>

      {/* Services */}
      <section id="services" className="bg-secondary/60 py-24 md:py-32">
        <div className="mx-auto max-w-7xl px-5">
          <Reveal className="mx-auto max-w-2xl text-center">
            <p className={`${EYEBROW} text-primary`}>Our services</p>
            <h2 className="mt-4 text-3xl font-extrabold md:text-5xl">
              Expert dental care for every need
            </h2>
            <p className="mt-5 text-muted-foreground">
              From routine check-ups to smile makeovers — planned around your teeth, your comfort
              and your budget.
            </p>
          </Reveal>

          <div className="mt-14 grid gap-7 sm:grid-cols-2 lg:grid-cols-4">
            {SERVICES.map((s, i) => (
              <Reveal key={s.title} delay={i * 120}>
                <article className="card-lift group h-full overflow-hidden rounded-[1.5rem] bg-card shadow-soft">
                  <div className="relative h-44 overflow-hidden">
                    <img
                      src={s.image}
                      alt={s.title}
                      loading="lazy"
                      width={1200}
                      height={1200}
                      className="h-full w-full object-cover transition-transform duration-700 group-hover:scale-110"
                    />
                  </div>
                  <div className="p-7">
                    <span className="-mt-12 mb-4 inline-flex h-14 w-14 items-center justify-center rounded-2xl bg-primary text-primary-foreground shadow-lift">
                      <s.icon className="h-6 w-6" />
                    </span>
                    <h3 className="font-display text-lg font-bold">{s.title}</h3>
                    <p className="mt-3 text-sm text-muted-foreground">{s.text}</p>
                    <a
                      href="#contact"
                      className="mt-5 inline-flex items-center gap-1.5 text-xs font-bold tracking-[0.18em] text-primary uppercase"
                    >
                      Enquire <ArrowRight className="h-3.5 w-3.5" />
                    </a>
                  </div>
                </article>
              </Reveal>
            ))}
          </div>
        </div>
      </section>

      {/* Visit clinic banner */}
      <section id="clinic" className="relative overflow-hidden py-28 md:py-36">
        <img
          src={cosmeticDentistry}
          alt="Dental care at Dhanvantari Multispeciality Dental Clinic"
          loading="lazy"
          width={1200}
          height={1200}
          className="absolute inset-0 h-full w-full object-cover"
        />
        <div aria-hidden className="surface-hero absolute inset-0" />
        <Reveal className="relative mx-auto max-w-3xl px-5 text-center text-white">
          <p className={`${EYEBROW} text-primary`}>Visit clinic</p>
          <h2 className="mt-4 text-3xl font-extrabold md:text-5xl">
            Comprehensive dental care for all ages
          </h2>
          <p className="mt-5 text-white/80">
            Dhanvantari Nursing Home, 142/A, Shete Nagar, Laxmi Peth, Solapur – 413001
          </p>
          <div className="mt-9 flex flex-wrap justify-center gap-4">
            <a
              href={`tel:${PHONE}`}
              className="btn-accent inline-flex items-center gap-2 rounded-full px-7 py-3.5 text-sm font-semibold"
            >
              <Phone className="h-4 w-4" /> Call {PHONE}
            </a>
            <a
              href={MAP_URL}
              target="_blank"
              rel="noreferrer"
              className="btn-outline-light inline-flex items-center gap-2 rounded-full px-7 py-3.5 text-sm font-semibold"
            >
              Get directions
            </a>
          </div>
        </Reveal>
      </section>

      {/* Why us */}
      <section id="why" className="py-24 md:py-32">
        <div className="mx-auto max-w-7xl px-5">
          <Reveal className="mx-auto max-w-2xl text-center">
            <p className={`${EYEBROW} text-primary`}>Why choose us</p>
            <h2 className="mt-4 text-3xl font-extrabold md:text-5xl">
              A higher standard of dental care
            </h2>
            <p className="mt-5 text-muted-foreground">
              Advanced training, careful hands and a calm environment — so treatment feels simple
              and safe.
            </p>
          </Reveal>
          <div className="mt-14 grid gap-7 md:grid-cols-3">
            {WHY.map((w, i) => (
              <Reveal key={w.title} delay={i * 130}>
                <div className="card-lift h-full rounded-[1.5rem] border border-border bg-card p-8 text-center">
                  <span className="inline-flex h-16 w-16 items-center justify-center rounded-full bg-secondary">
                    <w.icon className="h-7 w-7 text-primary" />
                  </span>
                  <h3 className="mt-6 font-display text-xl font-bold">{w.title}</h3>
                  <p className="mt-3 text-sm text-muted-foreground">{w.text}</p>
                </div>
              </Reveal>
            ))}
          </div>
        </div>
      </section>

      {/* Doctor */}
      <section className="bg-secondary/60 py-24 md:py-32">
        <div className="mx-auto max-w-7xl px-5">
          <Reveal className="mx-auto max-w-2xl text-center">
            <p className={`${EYEBROW} text-primary`}>Meet your dentist</p>
            <h2 className="mt-4 text-3xl font-extrabold md:text-5xl">Dr. Sanika S. K. Phadke</h2>
          </Reveal>
          <div className="mt-14 grid items-center gap-14 lg:grid-cols-[0.9fr_1.1fr]">
            <Reveal from="left">
              <img
                src={doctorPhoto}
                alt="Dr. Sanika Phadke at Dhanvantari Multispeciality Dental Clinic"
                loading="lazy"
                width={1008}
                height={1312}
                className="w-full rounded-[2rem] object-cover shadow-lift"
              />
            </Reveal>
            <Reveal from="right" delay={120}>
              <div className="space-y-5">
                <p className="text-muted-foreground">
                  Dr. Sanika combines careful clinical dentistry with an eye for aesthetics. Every
                  visit begins with a proper diagnosis and a plain explanation of your options — so
                  you always know what is being done and why. Patients come to her for pain-free
                  routine treatment as much as for smile makeovers.
                </p>
                <div className="grid gap-4 sm:grid-cols-2">
                  {[
                    { icon: GraduationCap, t: "B.D.S. (MUHS)" },
                    { icon: Award, t: "Fellowship in General Dentistry" },
                    { icon: Smile, t: "Fellowship in Smile Designing" },
                    { icon: Sparkles, t: "Fellowship in Cosmetic Dentistry" },
                  ].map((q) => (
                    <div
                      key={q.t}
                      className="flex items-center gap-3 rounded-2xl border border-border bg-card p-4 text-sm font-medium"
                    >
                      <q.icon className="h-5 w-5 shrink-0 text-primary" /> {q.t}
                    </div>
                  ))}
                </div>
                <a
                  href={`tel:${PHONE}`}
                  className="btn-accent inline-flex items-center gap-2 rounded-full px-7 py-3.5 text-sm font-semibold"
                >
                  <Phone className="h-4 w-4" /> Book with Dr. Sanika
                </a>
              </div>
            </Reveal>
          </div>
        </div>
      </section>

      {/* Contact */}
      <section id="contact" className="py-24 md:py-32">
        <div className="mx-auto max-w-7xl px-5">
          <Reveal className="mx-auto max-w-2xl text-center">
            <p className={`${EYEBROW} text-primary`}>Contact us</p>
            <h2 className="mt-4 text-3xl font-extrabold md:text-5xl">Come in for a check-up</h2>
            <p className="mt-5 text-muted-foreground">
              Call or message us and we will find a time that suits you.
            </p>
          </Reveal>

          <div className="mt-14 grid gap-8 lg:grid-cols-[1fr_1.2fr]">
            <div className="space-y-6">
              {[
                { icon: Phone, title: "Call for appointment", body: PHONE, href: `tel:${PHONE}` },
                {
                  icon: MessageCircle,
                  title: "WhatsApp",
                  body: "Message us for a quick reply",
                  href: WHATSAPP,
                },
                {
                  icon: MapPin,
                  title: "Clinic address",
                  body: "Dhanvantari Nursing Home, 142/A, Shete Nagar, Laxmi Peth, Solapur – 413001",
                  href: MAP_URL,
                },
                {
                  icon: Clock,
                  title: "Timings",
                  body: "Consultations by appointment — please call ahead",
                  href: `tel:${PHONE}`,
                },
              ].map((c, i) => (
                <Reveal key={c.title} delay={i * 110}>
                  <a
                    href={c.href}
                    target={c.href.startsWith("http") ? "_blank" : undefined}
                    rel="noreferrer"
                    className="card-lift flex items-start gap-4 rounded-2xl border border-border bg-card p-6"
                  >
                    <span className="rounded-xl bg-secondary p-3">
                      <c.icon className="h-6 w-6 text-primary" />
                    </span>
                    <span>
                      <span className="block font-display font-bold">{c.title}</span>
                      <span className="mt-1 block text-sm text-muted-foreground">{c.body}</span>
                    </span>
                  </a>
                </Reveal>
              ))}
            </div>

            <Reveal from="right" delay={140}>
              <div className="h-full overflow-hidden rounded-[1.5rem] border border-border shadow-soft">
                <iframe
                  title="Dhanvantari Multispeciality Dental Clinic location map"
                  src="https://www.google.com/maps?q=Dhanvantari%20Nursing%20Home%2C%20Shete%20Nagar%2C%20Laxmi%20Peth%2C%20Solapur%20413001&output=embed"
                  loading="lazy"
                  className="h-[460px] w-full lg:h-full"
                />
              </div>
            </Reveal>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-primary-deep py-14 text-white">
        <div className="mx-auto grid max-w-7xl gap-10 px-5 md:grid-cols-3">
          <div>
            <div className="flex items-center gap-3">
              <img
                src={logo.url}
                alt="Dhanvantari Multispeciality Dental Clinic logo"
                loading="lazy"
                width={48}
                height={48}
                className="h-12 w-12 rounded-full bg-white"
              />
              <span className="font-display text-sm font-bold">
                Dhanvantari Multispeciality
                <span className="block text-xs font-medium text-white/70">Dental Clinic</span>
              </span>
            </div>
            <p className="mt-5 text-sm text-white/70">
              Expert dental care in Solapur — general dentistry, smile designing and cosmetic
              dentistry.
            </p>
          </div>
          <div>
            <h3 className="font-display text-sm font-bold tracking-[0.18em] uppercase">Explore</h3>
            <ul className="mt-4 space-y-2 text-sm text-white/70">
              {NAV.map((n) => (
                <li key={n.href}>
                  <a href={n.href} className="transition-colors hover:text-primary">
                    {n.label}
                  </a>
                </li>
              ))}
            </ul>
          </div>
          <div>
            <h3 className="font-display text-sm font-bold tracking-[0.18em] uppercase">Reach us</h3>
            <ul className="mt-4 space-y-3 text-sm text-white/70">
              <li>
                <a href={`tel:${PHONE}`} className="hover:text-primary">
                  📞 {PHONE}
                </a>
              </li>
              <li>
                <a href={MAP_URL} target="_blank" rel="noreferrer" className="hover:text-primary">
                  📍 142/A, Shete Nagar, Laxmi Peth, Solapur – 413001
                </a>
              </li>
              <li>Dr. Sanika Sudha Kiranchandra Phadke, B.D.S. (MUHS)</li>
            </ul>
          </div>
        </div>
        <div className="mx-auto mt-12 max-w-7xl border-t border-white/15 px-5 pt-6 text-center text-xs text-white/55">
          © {new Date().getFullYear()} Dhanvantari Multispeciality Dental Clinic, Solapur
        </div>
      </footer>

      {/* Floating call */}
      <a
        href={`tel:${PHONE}`}
        className="btn-accent fixed right-5 bottom-5 z-40 inline-flex items-center gap-2 rounded-full px-5 py-3.5 text-sm font-semibold shadow-lift lg:hidden"
      >
        <Phone className="h-4 w-4" /> Call now
      </a>
    </div>
  );
}
