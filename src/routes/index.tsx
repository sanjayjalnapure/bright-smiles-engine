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
  ArrowRight,
  Check,
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
          "Gentle, modern dental care in Solapur. General dentistry, smile designing and cosmetic dentistry by Dr. Sanika Phadke, B.D.S. Call 9168362233.",
      },
      { property: "og:title", content: "Dhanvantari Dental Clinic Solapur | Dr. Sanika Phadke" },
      {
        property: "og:description",
        content:
          "General dentistry, smile designing and cosmetic dentistry at Shete Nagar, Laxmi Peth, Solapur.",
      },
    ],
  }),
  component: Home,
});

const PHONE = "9168362233";
const MAP_URL = "https://maps.app.goo.gl/mwtY7YMqPcS7rMus8";

const NAV = [
  { label: "Home", href: "#home" },
  { label: "About", href: "#about" },
  { label: "Services", href: "#services" },
  { label: "Clinic", href: "#clinic" },
  { label: "Contact", href: "#contact" },
];

const SERVICES = [
  {
    title: "General Dentistry",
    image: generalDentistry,
    icon: Stethoscope,
    text: "Routine check-ups, cleaning, fillings, root canal treatment and extractions — done gently and hygienically.",
    points: ["Scaling & polishing", "Tooth-coloured fillings", "Root canal treatment"],
  },
  {
    title: "Smile Designing",
    image: smileDesign,
    icon: Smile,
    text: "A smile planned around your face — shape, shade and proportion balanced so the result still looks like you.",
    points: ["Digital smile planning", "Teeth reshaping", "Gum contouring"],
  },
  {
    title: "Cosmetic Dentistry",
    image: cosmeticDentistry,
    icon: Sparkles,
    text: "Veneers, whitening and ceramic crowns using precise, tooth-friendly techniques for a natural finish.",
    points: ["Veneers & laminates", "Teeth whitening", "Ceramic crowns"],
  },
];

const WHY = [
  {
    icon: ShieldCheck,
    title: "Strict sterilisation",
    text: "Single-use disposables and autoclaved instruments for every single patient.",
  },
  {
    icon: GraduationCap,
    title: "Fellowship-trained",
    text: "Advanced training in general dentistry and in smile design & cosmetic dentistry.",
  },
  {
    icon: Smile,
    title: "Painless approach",
    text: "Calm, unhurried treatment with clear explanation before anything begins.",
  },
  {
    icon: Award,
    title: "Honest treatment plans",
    text: "Only what your teeth actually need, with the cost explained upfront.",
  },
];

function Home() {
  const [scrolled, setScrolled] = useState(false);
  const [open, setOpen] = useState(false);

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 24);
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  return (
    <div id="home" className="min-h-screen bg-background">
      {/* Header */}
      <header
        className={`fixed inset-x-0 top-0 z-50 transition-all duration-500 ${
          scrolled
            ? "bg-background/90 py-2 shadow-soft backdrop-blur-md"
            : "bg-transparent py-4 md:py-6"
        }`}
      >
        <div className="mx-auto flex max-w-7xl items-center justify-between px-5">
          <a href="#home" className="flex items-center gap-3">
            <img
              src={logo.url}
              alt="Dhanvantari Multispeciality Dental Clinic logo"
              width={56}
              height={56}
              className="h-12 w-12 rounded-full md:h-14 md:w-14"
            />
            <span className="hidden leading-tight sm:block">
              <span
                className={`block font-display text-sm font-bold md:text-base ${
                  scrolled ? "text-foreground" : "text-white"
                }`}
              >
                Dhanvantari Multispeciality
              </span>
              <span
                className={`block text-xs tracking-[0.2em] uppercase ${
                  scrolled ? "text-muted-foreground" : "text-white/75"
                }`}
              >
                Dental Clinic
              </span>
            </span>
          </a>

          <nav className="hidden items-center gap-8 lg:flex">
            {NAV.map((n) => (
              <a
                key={n.href}
                href={n.href}
                className={`relative text-sm font-medium after:absolute after:-bottom-1 after:left-0 after:h-0.5 after:w-full after:origin-bottom-right after:scale-x-0 after:bg-accent after:transition-transform after:duration-300 hover:after:origin-bottom-left hover:after:scale-x-100 ${
                  scrolled ? "text-foreground" : "text-white"
                }`}
              >
                {n.label}
              </a>
            ))}
            <a
              href={`tel:${PHONE}`}
              className="btn-accent inline-flex items-center gap-2 rounded-full px-5 py-2.5 text-sm font-semibold"
            >
              <Phone className="h-4 w-4" /> {PHONE}
            </a>
          </nav>

          <button
            aria-label="Menu"
            onClick={() => setOpen((v) => !v)}
            className={`lg:hidden ${scrolled ? "text-foreground" : "text-white"}`}
          >
            {open ? <X className="h-7 w-7" /> : <Menu className="h-7 w-7" />}
          </button>
        </div>

        {open && (
          <div className="mx-5 mt-3 rounded-2xl bg-card p-4 shadow-soft lg:hidden">
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
              <Phone className="h-4 w-4" /> Call {PHONE}
            </a>
          </div>
        )}
      </header>

      {/* Hero */}
      <section className="surface-hero relative overflow-hidden pt-32 pb-24 md:pt-44 md:pb-32">
        <div
          aria-hidden
          className="animate-float absolute -top-24 -right-24 h-96 w-96 rounded-full bg-white/10 blur-3xl"
        />
        <div
          aria-hidden
          className="absolute -bottom-32 -left-20 h-80 w-80 rounded-full bg-accent/20 blur-3xl"
        />
        <div className="relative mx-auto grid max-w-7xl items-center gap-14 px-5 lg:grid-cols-2">
          <div>
            <Reveal>
              <span className="inline-flex items-center gap-2 rounded-full border border-white/25 bg-white/10 px-4 py-1.5 text-xs font-semibold tracking-[0.16em] text-white uppercase">
                <Sparkles className="h-3.5 w-3.5" /> Solapur · Laxmi Peth
              </span>
            </Reveal>
            <Reveal delay={100}>
              <h1 className="mt-6 text-4xl leading-[1.08] font-extrabold text-white md:text-6xl">
                A healthy smile,
                <br />
                <span className="text-gradient-accent">designed for you</span>
              </h1>
            </Reveal>
            <Reveal delay={200}>
              <p className="mt-6 max-w-xl text-base text-white/80 md:text-lg">
                Dhanvantari Multispeciality Dental Clinic offers gentle general dentistry, smile
                designing and cosmetic dentistry under the care of Dr. Sanika Sudha Kiranchandra
                Phadke, B.D.S. (MUHS).
              </p>
            </Reveal>
            <Reveal delay={300}>
              <div className="mt-9 flex flex-wrap gap-4">
                <a
                  href={`tel:${PHONE}`}
                  className="btn-accent inline-flex items-center gap-2 rounded-full px-7 py-3.5 text-sm font-semibold"
                >
                  Book an appointment <ArrowRight className="h-4 w-4" />
                </a>
                <a
                  href="#services"
                  className="btn-outline-light inline-flex items-center gap-2 rounded-full px-7 py-3.5 text-sm font-semibold"
                >
                  Our treatments
                </a>
              </div>
            </Reveal>
            <Reveal delay={400}>
              <dl className="mt-12 grid max-w-lg grid-cols-3 gap-6 border-t border-white/15 pt-8">
                {[
                  { n: 3000, s: "+", l: "Smiles treated" },
                  { n: 10, s: "+", l: "Years of care" },
                  { n: 100, s: "%", l: "Sterile protocol" },
                ].map((s) => (
                  <div key={s.l}>
                    <dt className="font-display text-2xl font-bold text-accent md:text-3xl">
                      <Counter to={s.n} suffix={s.s} />
                    </dt>
                    <dd className="mt-1 text-xs text-white/70 md:text-sm">{s.l}</dd>
                  </div>
                ))}
              </dl>
            </Reveal>
          </div>

          <Reveal from="scale" delay={200}>
            <div className="relative">
              <img
                src={heroClinic}
                alt="Treatment room at Dhanvantari Multispeciality Dental Clinic"
                width={1600}
                height={1104}
                className="w-full rounded-[2rem] shadow-lift"
              />
              <div className="absolute -bottom-6 -left-4 hidden max-w-xs items-center gap-3 rounded-2xl bg-card p-4 shadow-lift sm:flex">
                <span className="rounded-xl bg-secondary p-2.5">
                  <ShieldCheck className="h-6 w-6 text-primary" />
                </span>
                <p className="text-sm font-medium">
                  Fully sterilised, modern equipment for every visit
                </p>
              </div>
            </div>
          </Reveal>
        </div>
      </section>

      {/* Marquee */}
      <div className="overflow-hidden border-y border-border bg-secondary py-4">
        <div className="animate-marquee flex w-max gap-10 whitespace-nowrap">
          {[...Array(2)].map((_, dup) => (
            <div key={dup} className="flex gap-10">
              {[
                "General Dentistry",
                "Smile Designing",
                "Cosmetic Dentistry",
                "Root Canal Treatment",
                "Teeth Whitening",
                "Veneers & Crowns",
              ].map((t) => (
                <span
                  key={t}
                  className="flex items-center gap-3 text-sm font-semibold tracking-wide text-secondary-foreground uppercase"
                >
                  <span className="h-1.5 w-1.5 rounded-full bg-accent" /> {t}
                </span>
              ))}
            </div>
          ))}
        </div>
      </div>

      {/* About */}
      <section id="about" className="py-24 md:py-32">
        <div className="mx-auto grid max-w-7xl items-center gap-14 px-5 lg:grid-cols-2">
          <Reveal from="left">
            <div className="relative">
              <img
                src={doctorPhoto}
                alt="Dr. Sanika Phadke at the clinic"
                loading="lazy"
                width={1008}
                height={1312}
                className="w-full rounded-[2rem] object-cover shadow-lift"
              />
              <div className="absolute -right-4 bottom-8 hidden rounded-2xl bg-primary p-5 text-primary-foreground shadow-lift md:block">
                <p className="font-display text-lg font-bold">B.D.S. (MUHS)</p>
                <p className="text-xs text-primary-foreground/75">Fellowship trained</p>
              </div>
            </div>
          </Reveal>

          <div>
            <Reveal>
              <p className="text-xs font-semibold tracking-[0.2em] text-primary uppercase">
                Meet your dentist
              </p>
              <h2 className="mt-4 text-3xl font-extrabold md:text-4xl">
                Dr. Sanika Sudha Kiranchandra Phadke
              </h2>
              <p className="mt-5 text-muted-foreground">
                Dr. Sanika combines careful clinical dentistry with an eye for aesthetics. Every
                treatment begins with a proper diagnosis and a plain explanation of your options —
                so you always know what is being done and why. Patients come to her for pain-free
                routine care as much as for smile makeovers.
              </p>
            </Reveal>
            <div className="mt-8 space-y-4">
              {[
                "B.D.S. (MUHS)",
                "Fellowship in General Dentistry",
                "Fellowship in Smile Designing & Cosmetic Dentistry",
              ].map((q, i) => (
                <Reveal key={q} delay={i * 120}>
                  <div className="flex items-center gap-4 rounded-xl border border-border bg-card p-4 card-lift">
                    <span className="rounded-lg bg-secondary p-2">
                      <Check className="h-5 w-5 text-primary" />
                    </span>
                    <span className="font-medium">{q}</span>
                  </div>
                </Reveal>
              ))}
            </div>
            <Reveal delay={360}>
              <a
                href="#contact"
                className="mt-9 inline-flex items-center gap-2 rounded-full bg-primary px-7 py-3.5 text-sm font-semibold text-primary-foreground transition-transform duration-300 hover:-translate-y-0.5"
              >
                Visit the clinic <ArrowRight className="h-4 w-4" />
              </a>
            </Reveal>
          </div>
        </div>
      </section>

      {/* Services */}
      <section id="services" className="bg-secondary/50 py-24 md:py-32">
        <div className="mx-auto max-w-7xl px-5">
          <Reveal className="mx-auto max-w-2xl text-center">
            <p className="text-xs font-semibold tracking-[0.2em] text-primary uppercase">
              What we do
            </p>
            <h2 className="mt-4 text-3xl font-extrabold md:text-4xl">
              Dental care for every stage
            </h2>
            <p className="mt-4 text-muted-foreground">
              From a simple cleaning to a full smile makeover, treatments are planned around your
              teeth, your comfort and your budget.
            </p>
          </Reveal>

          <div className="mt-14 grid gap-8 md:grid-cols-3">
            {SERVICES.map((s, i) => (
              <Reveal key={s.title} delay={i * 140}>
                <article className="card-lift group h-full overflow-hidden rounded-[1.5rem] bg-card shadow-soft">
                  <div className="relative h-52 overflow-hidden">
                    <img
                      src={s.image}
                      alt={s.title}
                      loading="lazy"
                      width={1200}
                      height={1200}
                      className="h-full w-full object-cover transition-transform duration-700 group-hover:scale-110"
                    />
                    <span className="absolute bottom-4 left-4 rounded-xl bg-card/90 p-2.5 backdrop-blur">
                      <s.icon className="h-5 w-5 text-primary" />
                    </span>
                  </div>
                  <div className="p-7">
                    <h3 className="font-display text-xl font-bold">{s.title}</h3>
                    <p className="mt-3 text-sm text-muted-foreground">{s.text}</p>
                    <ul className="mt-5 space-y-2">
                      {s.points.map((p) => (
                        <li key={p} className="flex items-center gap-2 text-sm">
                          <span className="h-1.5 w-1.5 rounded-full bg-accent" /> {p}
                        </li>
                      ))}
                    </ul>
                  </div>
                </article>
              </Reveal>
            ))}
          </div>
        </div>
      </section>

      {/* Why us */}
      <section className="py-24 md:py-32">
        <div className="mx-auto max-w-7xl px-5">
          <Reveal className="mx-auto max-w-2xl text-center">
            <p className="text-xs font-semibold tracking-[0.2em] text-primary uppercase">
              Why patients choose us
            </p>
            <h2 className="mt-4 text-3xl font-extrabold md:text-4xl">
              Careful hands, clear answers
            </h2>
          </Reveal>
          <div className="mt-14 grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
            {WHY.map((w, i) => (
              <Reveal key={w.title} delay={i * 120}>
                <div className="card-lift h-full rounded-2xl border border-border bg-card p-7">
                  <span className="inline-flex rounded-xl bg-secondary p-3">
                    <w.icon className="h-6 w-6 text-primary" />
                  </span>
                  <h3 className="mt-5 font-display text-lg font-bold">{w.title}</h3>
                  <p className="mt-2 text-sm text-muted-foreground">{w.text}</p>
                </div>
              </Reveal>
            ))}
          </div>
        </div>
      </section>

      {/* Clinic */}
      <section id="clinic" className="surface-hero relative overflow-hidden py-24 md:py-32">
        <div className="relative mx-auto grid max-w-7xl items-center gap-14 px-5 lg:grid-cols-2">
          <Reveal from="left">
            <img
              src={clinicEntrance.url}
              alt="Entrance of Dhanvantari Multispeciality Dental Clinic in Solapur"
              loading="lazy"
              width={1200}
              height={860}
              className="w-full rounded-[2rem] shadow-lift"
            />
          </Reveal>
          <Reveal from="right" delay={120}>
            <div className="text-white">
              <p className="text-xs font-semibold tracking-[0.2em] text-accent uppercase">
                Our clinic
              </p>
              <h2 className="mt-4 text-3xl font-extrabold md:text-4xl">
                Right inside Dhanvantari Nursing Home
              </h2>
              <p className="mt-5 text-white/80">
                A calm, air-conditioned clinic at Shete Nagar, Laxmi Peth — easy to reach from
                anywhere in Solapur, with a modern dental chair, digital diagnostics and a
                thoroughly sterilised setup.
              </p>
              <div className="mt-8 space-y-4">
                <div className="flex items-start gap-4 rounded-2xl bg-white/10 p-5 backdrop-blur">
                  <MapPin className="mt-0.5 h-5 w-5 shrink-0 text-accent" />
                  <p className="text-sm">
                    Dhanvantari Nursing Home, 142/A, Shete Nagar, Laxmi Peth, Solapur, Maharashtra –
                    413001
                  </p>
                </div>
                <div className="flex items-start gap-4 rounded-2xl bg-white/10 p-5 backdrop-blur">
                  <Clock className="mt-0.5 h-5 w-5 shrink-0 text-accent" />
                  <p className="text-sm">
                    Consultations by appointment — please call ahead to confirm your slot.
                  </p>
                </div>
              </div>
              <a
                href={MAP_URL}
                target="_blank"
                rel="noreferrer"
                className="btn-accent mt-8 inline-flex items-center gap-2 rounded-full px-7 py-3.5 text-sm font-semibold"
              >
                Get directions <ArrowRight className="h-4 w-4" />
              </a>
            </div>
          </Reveal>
        </div>
      </section>

      {/* Contact */}
      <section id="contact" className="py-24 md:py-32">
        <div className="mx-auto max-w-7xl px-5">
          <Reveal className="mx-auto max-w-2xl text-center">
            <p className="text-xs font-semibold tracking-[0.2em] text-primary uppercase">
              Appointments
            </p>
            <h2 className="mt-4 text-3xl font-extrabold md:text-4xl">Come in for a check-up</h2>
            <p className="mt-4 text-muted-foreground">
              Call or message us and we will find a time that suits you.
            </p>
          </Reveal>

          <div className="mt-14 grid gap-8 lg:grid-cols-[1fr_1.2fr]">
            <div className="space-y-6">
              {[
                {
                  icon: Phone,
                  title: "Call for appointment",
                  body: PHONE,
                  href: `tel:${PHONE}`,
                },
                {
                  icon: MapPin,
                  title: "Clinic address",
                  body: "142/A, Shete Nagar, Laxmi Peth, Solapur – 413001",
                  href: MAP_URL,
                },
              ].map((c, i) => (
                <Reveal key={c.title} delay={i * 130}>
                  <a
                    href={c.href}
                    target={c.href.startsWith("http") ? "_blank" : undefined}
                    rel="noreferrer"
                    className="card-lift flex items-start gap-4 rounded-2xl border border-border bg-card p-7"
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
              <Reveal delay={260}>
                <div className="rounded-2xl surface-hero p-7 text-white">
                  <h3 className="font-display text-lg font-bold">
                    Dhanvantari Multispeciality Dental Clinic
                  </h3>
                  <p className="mt-2 text-sm text-white/80">
                    Dr. Sanika Sudha Kiranchandra Phadke, B.D.S. (MUHS) · General Dentistry · Smile
                    Designing · Cosmetic Dentistry
                  </p>
                </div>
              </Reveal>
            </div>

            <Reveal from="right" delay={140}>
              <div className="h-full overflow-hidden rounded-[1.5rem] border border-border shadow-soft">
                <iframe
                  title="Dhanvantari Multispeciality Dental Clinic location map"
                  src="https://www.google.com/maps?q=Dhanvantari%20Nursing%20Home%2C%20Shete%20Nagar%2C%20Laxmi%20Peth%2C%20Solapur%20413001&output=embed"
                  loading="lazy"
                  className="h-[420px] w-full lg:h-full"
                />
              </div>
            </Reveal>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="border-t border-border bg-secondary/50 py-10">
        <div className="mx-auto flex max-w-7xl flex-col items-center gap-4 px-5 text-center md:flex-row md:justify-between md:text-left">
          <div className="flex items-center gap-3">
            <img
              src={logo.url}
              alt="Dhanvantari Multispeciality Dental Clinic logo"
              loading="lazy"
              width={44}
              height={44}
              className="h-11 w-11 rounded-full"
            />
            <span className="text-sm font-semibold">
              Dhanvantari Multispeciality Dental Clinic, Solapur
            </span>
          </div>
          <p className="text-xs text-muted-foreground">
            © {new Date().getFullYear()} Dhanvantari Multispeciality Dental Clinic · Appointments{" "}
            {PHONE}
          </p>
        </div>
      </footer>

      {/* Mobile call bar */}
      <a
        href={`tel:${PHONE}`}
        className="btn-accent fixed right-5 bottom-5 z-40 inline-flex items-center gap-2 rounded-full px-5 py-3.5 text-sm font-semibold shadow-lift lg:hidden"
      >
        <Phone className="h-4 w-4" /> Call now
      </a>
    </div>
  );
}
